```py
class SoftwareEngineer(metaclass=DevOps):
    """
    Software Engineer with 5+ years of experience in enterprise telecom environments.
    Specializes in both backend and frontend development including OPS batteries.
    Passionate about getting to know anything i don't know and
        always open to new opportunities to learn, create, and improve.
    """

    languages: List[str] = ["Python", "JS/TS", "PL/SQL"]  # but also language-agnostic
    speaks: List[str] = ["English", "Estonian", "Russian"]
    frameworks: List[str] = ["FastAPI", "Pyramid", "Angular", "Vue", "React"]
    os: List[str] = ["Debian", "Ubuntu", "NixOS", "Hyprland"]
    skills: List[str] = ["k8s", "docker", "linux", "ci/cd", "kafka", "rabbitmq",
                         "grafana", "node.js", "redis", "nginx", "sqlalchemy",
                         "postgresql", "SOLID", "agile", "SAFe", "distributed processing"]
    focus: List[str] = [
        "Reliable and scalable systems",
        "Performant code",
        "Security in mind",
        "Spend hours automating anything taking over 30sec of manual labor"
    ]

    @property
    def hobbies(self):
        for hobby in ["Gaming", "Modding", "Piano", "Table Tennis"]:
            if now() == "3 am":
                yield "Coding"
            
            yield hobby

    async def stats(self):
        return """
        ┌────────────────────────────────────┐
        │      📊top       32📁 23⭐ 405✏️ │
        ├─────────────────┬──────────────────┤
        │ #1  TypeScript  │ 44.2% (297.5 KB) │
        │ #2  Python      │ 29.1% (195.6 KB) │
        │ #3  JavaScript  │  8.0% (53.5 KB ) │
        │ #4  CSS         │  4.4% (29.7 KB ) │
        │ #5  Rust        │  3.9% (26.5 KB ) │
        │ #6  C#          │  3.4% (23.1 KB ) │
        │ #7  C++         │  3.1% (20.6 KB ) │
        │ #8  SourcePawn  │  1.5% (9.9 KB  ) │
        │ #9  HTML        │  1.2% (8.2 KB  ) │
        │ #10 Squirrel    │  1.2% (7.9 KB  ) │
        └─────────────────┴──────────────────┘
        """

    @staticmethod
    def sleep():
        raise NotImplementedError("sleep is not implemented, keep working!")

#TODO: rewrite this in Rust...
```
