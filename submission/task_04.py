"""Task 04 — Next version (SemVer & Commits) (submission copy)

Копія реалізації для здачі: next_version(current_version, commits)
"""
import re
from typing import List

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def _is_valid_commit_message(msg: str) -> bool:
    if "BREAKING" in msg or "!:" in msg or msg.startswith("feat!"):
        return True
    return bool(re.match(r"^(feat|fix|docs|perf|chore|refactor|style)(?:\([^)]*\))?:", msg))


def next_version(current_version: str, commits: List[str]) -> str:
    if not isinstance(current_version, str):
        raise ValueError("Invalid version")
    m = SEMVER_RE.match(current_version)
    if not m:
        raise ValueError("Invalid version")

    if not isinstance(commits, list):
        raise ValueError("Invalid commits")

    major, minor, patch = map(int, m.groups())

    breaking = False
    has_feat = False
    has_fix = False

    for c in commits:
        if not isinstance(c, str):
            raise ValueError("Invalid commits")
        if not _is_valid_commit_message(c):
            raise ValueError(f"Некоректне повідомлення: {c}")
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
        patch += 1

    return f"{major}.{minor}.{patch}"
