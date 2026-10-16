"""Task 04 — Next version (SemVer & Commits)

Функція next_version(current_version: str, commits: list[str]) -> str
Парсить SemVer у форматі MAJOR.MINOR.PATCH і інкрементує згідно правил:
- Якщо є breaking change (рядок містить "BREAKING" або починається з "feat!" або має "!:"), то MAJOR++
- Інакше якщо є commit, який починається з "feat" -> MINOR++
- Інакше якщо є commit, який починається з "fix" або "perf" -> PATCH++
- Інакше PATCH++ (щоб бути консервативним)

На некоректний формат версії кидає ValueError("Invalid version").
На некоректний commits кидає ValueError("Invalid commits").
"""
import re
from typing import List

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def next_version(current_version: str, commits: List[str]) -> str:
    if not isinstance(current_version, str):
        raise ValueError("Invalid version")
    m = SEMVER_RE.match(current_version)
    if not m:
        raise ValueError("Invalid version")

    if not isinstance(commits, list):
        raise ValueError("Invalid commits")

    major, minor, patch = map(int, m.groups())

    # detect breaking
    breaking = False
    has_feat = False
    has_fix = False

    for c in commits:
        if not isinstance(c, str):
            raise ValueError("Invalid commits")
        if "BREAKING" in c or c.startswith("feat!") or "!:" in c:
            breaking = True
            break
        if c.startswith("feat"):
            has_feat = True
        if c.startswith("fix") or c.startswith("perf"):
            has_fix = True

    if breaking:
        major += 1
        minor = 0
        patch = 0
    elif has_feat:
        minor += 1
        patch = 0
    else:
        # if any fix or none of the other rules, bump patch
        patch += 1

    return f"{major}.{minor}.{patch}"
