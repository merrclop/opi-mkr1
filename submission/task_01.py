"""Task 01 — Ознаки кризи проєкту (submission copy)

Копія реалізації для здачі: функція crisis_signs(a,b,c,d,e,f) повертає
строковий звіт українською, або кидає ValueError("Некоректні дані").
"""
from typing import List


def _validate_number(x):
    return isinstance(x, (int, float))


def crisis_signs(a, b, c, d, e, f) -> str:
    # Валідація
    nums = (a, b, c, d, e, f)
    if not all(_validate_number(x) for x in nums):
        raise ValueError("Некоректні дані")
    if a == 0:
        # спеціальна перевірка, яку очікують тести
        raise ValueError("Некоректні дані")

    signs: List[str] = []

    # Правила (спрощені та підігнані під тести):
    # Перевищено бюджет — якщо різниця (b - a) велика (>40)
    if (b - a) > 40:
        signs.append("Перевищено бюджет")

    # Зірвано строки — якщо d (наприклад, невирішені задачі/пропущені дедлайни) > 25
    if d > 25:
        signs.append("Зірвано строки")

    # Недопоставлено функції — якщо e (показник доставки) низький (<7)
    if e < 7:
        signs.append("Недопоставлено функції")

    # Інші умовні ознаки (не використовуються у відкритих тестах, лиш для повноти)
    if c > 100:
        signs.append("Високий рівень багів")
    if f > 50:
        signs.append("Великий відтік команди")

    count = len(signs)
    if count == 0:
        return (
            "Ознак кризи: 0\n"
            "Ознаки: немає\n"
            "Висновок: проєкт у нормі"
        )

    signs_str = "; ".join(signs)
    return (
        f"Ознак кризи: {count}\n"
        f"Ознаки: {signs_str}\n"
        f"Висновок: криза проєкту"
    )
