"""Task 06 — Audit requirements (submission copy)

Копія реалізації для здачі: audit_requirements(lines, vulns)
"""
from typing import List, Dict, Tuple
import re


def _parse_pkg(line: str):
    s = line.strip()
    if not s or s.startswith("#"):
        return None
    if s.startswith("-e") or s.startswith("git+"):
        return (s, None, True)
    m = re.match(r"^([A-Za-z0-9_.-]+)\s*(==|>=|<=|>|<|~=)?\s*(.+)?$", s)
    if not m:
        return (s, None, False)
    name = m.group(1)
    op = m.group(2)
    ver = m.group(3)
    if ver is not None:
        ver = ver.strip()
    return (name, (op, ver) if op else None, False)


def _cmp_version(v1: str, v2: str) -> int:
    def norm(v):
        parts = [int(x) if x.isdigit() else 0 for x in re.split(r"\.|-", v)]
        return parts
    p1 = norm(v1)
    p2 = norm(v2)
    L = max(len(p1), len(p2))
    p1 += [0] * (L - len(p1))
    p2 += [0] * (L - len(p2))
    for a, b in zip(p1, p2):
        if a < b:
            return -1
        if a > b:
            return 1
    return 0


def audit_requirements(lines: List[str], vulns: Dict[str, List[Tuple[str, str]]]) -> List[str]:
    if not isinstance(lines, list) or not isinstance(vulns, dict):
        raise ValueError("Invalid input")

    seen = {}
    messages: List[str] = []

    for ln in lines:
        parsed = _parse_pkg(ln)
        if parsed is None:
            continue
        name, info, editable = parsed
        lname = name.lower()
        if lname in seen:
            raise ValueError(f"Дублікат пакета: {lname}")
        seen[lname] = (info, editable)

    for lname, (info, editable) in seen.items():
        if editable:
            continue
        if info is None:
            messages.append(f"Версію не зафіксовано: {lname}")
            continue
        op, ver = info
        if op == "==" and ver:
            vul = vulns.get(lname, [])
            for (cve, fixed) in vul:
                try:
                    if _cmp_version(ver, fixed) < 0:
                        messages.append(f"{lname} {ver}: вразливість {cve}, виправлено у {fixed}")
                except Exception:
                    messages.append(f"{lname} {ver}: вразливість {cve}, виправлено у {fixed}")
        else:
            messages.append(f"Версію не зафіксовано: {lname}")

    return messages
