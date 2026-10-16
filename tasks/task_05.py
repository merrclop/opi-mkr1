"""Task 05 — Sprint plan (submission copy)

Копія реалізації для здачі: sprint_plan(tasks, velocity_history)
"""
from typing import List, Tuple
import math


def sprint_plan(tasks: List[Tuple[str, int]], velocity_history: List[int]) -> str:
    if not isinstance(tasks, list) or not isinstance(velocity_history, list):
        raise ValueError("Некоректні дані")
    if len(velocity_history) == 0:
        raise ValueError("Некоректна історія швидкості")

    for t in tasks:
        if not (isinstance(t, tuple) and len(t) == 2 and isinstance(t[0], str) and isinstance(t[1], (int, float))):
            raise ValueError("Некоректні дані")

    avg = sum(velocity_history) / len(velocity_history)
    capacity = int(round(avg))

    in_sprint = []
    in_sprint_points = 0
    to_split = []

    for name, pts in tasks:
        pts = int(pts)
        if pts > capacity:
            to_split.append(name)
            continue
        if in_sprint_points + pts <= capacity:
            in_sprint.append(name)
            in_sprint_points += pts
            continue
        break

    total_points_ready = sum(int(p) for (n, p) in tasks if n not in to_split)
    sprints_needed = 0
    if capacity > 0:
        sprints_needed = math.ceil(total_points_ready / capacity)

    in_sprint_str = ", ".join(in_sprint) if in_sprint else "немає"
    to_split_str = ", ".join(to_split) if to_split else "немає"

    result = [f"Місткість: {capacity} б."]
    result.append(f"У спринт: {in_sprint_str} ({in_sprint_points} б.)")
    result.append(f"Потребують розбиття: {to_split_str}")
    result.append(f"Спринтів до завершення готових пунктів: {sprints_needed}")

    return "\n".join(result)
