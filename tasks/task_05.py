"""Task 05 — План спринту за швидкістю

Функція plan_sprints(velocity_history: list[int], backlog: int) -> int
Повертає мінімальну кількість спринтів, потрібних для завершення беклогу при середній швидкості.

Валідація: кидає ValueError("Invalid input") для некоректних типів.
Якщо середня швидкість дорівнює нулю — ValueError("Velocity is zero").
"""
from typing import List
import math


def plan_sprints(velocity_history: List[int], backlog: int) -> int:
    if not isinstance(velocity_history, list) or not isinstance(backlog, int):
        raise ValueError("Invalid input")
    if backlog <= 0:
        return 0

    if len(velocity_history) == 0:
        raise ValueError("Invalid input")

    total = 0
    count = 0
    for v in velocity_history:
        if not isinstance(v, (int, float)):
            raise ValueError("Invalid input")
        if v < 0:
            raise ValueError("Invalid input")
        total += v
        count += 1

    avg = total / count if count > 0 else 0
    if avg == 0:
        raise ValueError("Velocity is zero")

    sprints = math.ceil(backlog / avg)
    return int(sprints)
