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
        │      📊top       38📁 22⭐ 488✏️ │
        ├─────────────────┬──────────────────┤
        │ #1  C           │ 90.1% (15.88 MB) │
        │ #2  C++         │  4.5% (784.9 KB) │
        │ #3  TypeScript  │  2.0% (360.3 KB) │
        │ #4  Python      │  1.2% (211.7 KB) │
        │ #5  GLSL        │  0.4% (72.7 KB ) │
        │ #6  JavaScript  │  0.3% (53.5 KB ) │
        │ #7  CSS         │  0.2% (40.6 KB ) │
        │ #8  Makefile    │  0.2% (35.8 KB ) │
        │ #9  Rust        │  0.1% (26.5 KB ) │
        │ #10 Shell       │  0.1% (25.9 KB ) │
        └─────────────────┴──────────────────┘
        """

    @staticmethod
    def sleep():
        raise NotImplementedError("sleep is not implemented, keep working!")

#TODO: rewrite this in Rust...
```
