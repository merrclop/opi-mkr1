"""Task 01 — Ознаки кризи проєкту

Функція detect_crisis приймає словник метрик проекту і повертає список знайдених ознак кризи.
Правила (приклад):
- низька швидкість (velocity < 3)
- високий рівень багів (bug_rate > 0.1)
- високий відтік (team_turnover > 0.2)
- зростання беклогу (unresolved_issues > 100)
- пропущені дедлайни (overdue_percent > 0.2)

Поведінка при некоректних даних: кидає ValueError("Invalid input").

Обмеження: тільки стандартна бібліотека, немає print/input.
"""
from typing import Dict, List


def detect_crisis(metrics: Dict) -> List[str]:
    """Аналізує словник метрик та повертає список ознак кризи.

    Очікується, що metrics — це dict з числовими значеннями для ключів,
    наприклад: velocity, bug_rate, team_turnover, unresolved_issues, overdue_percent.

    Повертає список рядків (може бути порожній список).
    """
    if not isinstance(metrics, dict):
        raise ValueError("Invalid input")

    signs = []

    try:
        velocity = metrics.get("velocity")
        if velocity is not None:
            if not isinstance(velocity, (int, float)):
                raise ValueError("Invalid input")
            if velocity < 3:
                signs.append("low_velocity")

        bug_rate = metrics.get("bug_rate")
        if bug_rate is not None:
            if not isinstance(bug_rate, (int, float)):
                raise ValueError("Invalid input")
            if bug_rate > 0.1:
                signs.append("high_bug_rate")

        team_turnover = metrics.get("team_turnover")
        if team_turnover is not None:
            if not isinstance(team_turnover, (int, float)):
                raise ValueError("Invalid input")
            if team_turnover > 0.2:
                signs.append("high_turnover")

        unresolved = metrics.get("unresolved_issues")
        if unresolved is not None:
            if not isinstance(unresolved, (int, float)):
                raise ValueError("Invalid input")
            if unresolved > 100:
                signs.append("backlog_growth")

        overdue = metrics.get("overdue_percent")
        if overdue is not None:
            if not isinstance(overdue, (int, float)):
                raise ValueError("Invalid input")
            if overdue > 0.2:
                signs.append("missed_deadlines")

    except KeyError:
        raise ValueError("Invalid input")

    return signs
