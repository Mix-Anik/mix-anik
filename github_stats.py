import os
import requests
from datetime import datetime, timezone


TOKEN = os.getenv("PAT_TOKEN")
IDENT = " " * 8

if not TOKEN:
    raise ValueError("Set your GITHUB_TOKEN as environment variable")

HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
GRAPHQL_URL = "https://api.github.com/graphql"


def run_query(query, variables=None):
    resp = requests.post(GRAPHQL_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()

    if "errors" in data:
        raise ValueError(f"GraphQL errors: {data['errors']}")

    return data


def iter_query_nodes(query, path: list[str], variables=None):
    variables = {**(variables or {}), "cursor": None}

    while True:
        data = run_query(query, variables)
        connection = data["data"]

        for key in path:
            connection = connection[key]

        yield from connection["nodes"]

        if not connection["pageInfo"]["hasNextPage"]:
            break

        variables["cursor"] = connection["pageInfo"]["endCursor"]


def get_repos_data(affiliations) -> dict:
    query = """
    query($cursor: String, $affiliations: [RepositoryAffiliation]) {
        viewer {
            repositories(ownerAffiliations: $affiliations, first: 100, after: $cursor) {
                totalCount
                pageInfo {
                    hasNextPage
                    endCursor
                }
                nodes {
                    name
                    isPrivate
                    isFork
                    stargazerCount
                    viewerPermission
                    languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
                        edges {
                            size
                            node {
                                name
                                color
                            }
                        }
                    }
                }
            }
        }
    }
    """

    count = 0
    stars = 0
    language_bytes = {}
    for repo_data in iter_query_nodes(query, path=["viewer", "repositories"], variables={'affiliations': affiliations}):
        if repo_data['viewerPermission'] == 'ADMIN':
            count += 1
            stars += repo_data['stargazerCount']
        
        if not repo_data['isFork'] and repo_data['viewerPermission'] == 'ADMIN':
            for edge in repo_data["languages"]["edges"]:
                language_bytes.setdefault(edge["node"]["name"], 0)
                language_bytes[edge["node"]["name"]] += edge["size"]
    
    sorted_langs = sorted(language_bytes.items(), key=lambda x: x[1], reverse=True)
    total_bytes = sum(language_bytes.values())
    lang_data = [(lang, sz, round(sz / total_bytes * 100, 2)) for lang, sz in sorted_langs[:10]]

    return {"total_count": count, "total_stars": stars, "lang": lang_data}


def get_commits_data() -> int:
    query = """
    query($from: DateTime!, $to: DateTime!) {
        viewer {
            contributionsCollection(from: $from, to: $to) {
                totalCommitContributions
                restrictedContributionsCount
            }
        }
    }
    """

    total = 0
    for year in range(2018, datetime.now(timezone.utc).year + 1):
        data = run_query(query, variables={"from": f"{year}-01-01T00:00:00Z", "to": f"{year}-12-31T23:59:59Z"})
        collection = data["data"]["viewer"]["contributionsCollection"]
        total += collection["totalCommitContributions"] + collection["restrictedContributionsCount"]

    return total


def compose_stats_table(lang_data, header_stats) -> str:
    lines = []
    lines.append("┌────────────────────────────────────┐")
    lines.append(f"│       top{header_stats:>22} │")
    lines.append("├─────────────────┬──────────────────┤")

    for idx, (lang, sz, pct) in enumerate(lang_data, 1):
        pct_fmt = f"{pct:.1f}%"

        if sz >= 1000000:
            sz_fmt = f"{sz / 1000000:.2f} MB"
        elif sz >= 1000:
            sz_fmt = f"{sz / 1000:.1f} KB"

        lines.append(f"│ #{idx:<2} {lang:<11} │ {pct_fmt:>5} ({sz_fmt:<8}) │")

    lines.append("└─────────────────┴──────────────────┘")
    return "\n".join([IDENT + l for l in lines])

owned_repos_data = get_repos_data(['OWNER'])
total_repos = owned_repos_data['total_count']
total_stars = owned_repos_data['total_stars']
total_commits = get_commits_data()
header_stats = f'{total_repos}📁 {total_stars}⭐ {total_commits}✏️'
table_str = compose_stats_table(owned_repos_data['lang'], header_stats)

with open('README.template', "r") as f:
    content = f.read()

content = content % {'GH_STATS': table_str}
with open('README.md', "w") as f:
    f.write(content)
