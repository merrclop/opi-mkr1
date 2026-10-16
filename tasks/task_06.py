"""Task 06 — Аудит requirements.txt (SCA)

Функція audit_requirements(lines: list[str]) -> dict
Аналізує список рядків з файлу requirements.txt та повертає словник з ключами:
- invalid: рядки, які не відповідають простому очікуваному формату
- editable: рядки, що встановлюються у режимі editable або з VCS (-e, git+)
- pinned: рядки з жорсткою фіксацією версії (==)

На некоректний вхід кидає ValueError("Invalid input").

Зверніть увагу: це спрощений аудит для навчальної мети.
"""
import re
from typing import List, Dict

PKG_RE = re.compile(r"^[A-Za-z0-9_.-]+([<>=!~]{1,2}.+)?$")


def audit_requirements(lines: List[str]) -> Dict[str, List[str]]:
    if not isinstance(lines, list):
        raise ValueError("Invalid input")

    invalid = []
    editable = []
    pinned = []

    for ln in lines:
        if not isinstance(ln, str):
            raise ValueError("Invalid input")
        s = ln.strip()
        if s == "" or s.startswith("#"):
            continue
        if s.startswith("-e") or s.startswith("git+"):
            editable.append(s)
            continue
        if "==" in s:
            pinned.append(s)
        # simple validation: package name with optional operator/version
        if not PKG_RE.match(s):
            invalid.append(s)

    return {"invalid": invalid, "editable": editable, "pinned": pinned}
