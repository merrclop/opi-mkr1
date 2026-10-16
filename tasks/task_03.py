"""Task 03 — Секрети в конфігурації

Функція secrets_report(lines: list[str]) -> list[str]
Повертає список рядків з повідомленнями про можливі секрети у форматі:
'Рядок {lineno}: можливий секрет у «{VAR}»'
Правила (спрощені для тестів):
- ігноруємо рядки що починаються з '#'
- ігноруємо посилання на змінні у вигляді ${...} та використання os.environ
- вважаємо можливим секретом ті рядки, де ліворуч від '=' знаходиться
  іменований параметр у верхньому регістрі, що містить 'PASSWORD' або 'TOKEN'
- при некоректному вхідному типі кидаємо ValueError("Некоректні дані")
"""
from typing import List
import re


def secrets_report(lines: List[str]) -> List[str]:
    if not isinstance(lines, list):
        raise ValueError("Некоректні дані")
    for ln in lines:
        if not isinstance(ln, str):
            raise ValueError("Некоректні дані")

    alerts: List[str] = []

    for i, ln in enumerate(lines, start=1):
        s = ln.strip()
        if not s or s.startswith('#'):
            continue
        # ignore ${...} and os.environ
        if '${' in s or 'os.environ' in s:
            continue
        # look for KEY=VALUE pattern
        if '=' not in s:
            continue
        key = s.split('=', 1)[0].strip()
        # consider only uppercase keys for secrets detection
        if key.isupper() and ("PASSWORD" in key or "TOKEN" in key):
            alerts.append(f"Рядок {i}: можливий секрет у «{key}»")
    return alerts
