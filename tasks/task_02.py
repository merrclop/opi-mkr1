"""Task 02 — Переходи між фазами (Каскад)

Функція check_history(model: str, history: list[str]) -> str
Повертає рядок-результат згідно з тестами:
- для 'каскад' заборонені будь-які кроки назад;
  при виявленні повертає 'Заборонений перехід: {prev} -> {curr} (крок {i})'
  де i — індекс (1-based) попереднього елементу у списку history.
- для 'каскад зі зворотним зв'язком' дозволені кроки назад, але повертається
  'Допустимо; кроків назад: {count}' — кількість назад переходів.

Простий набір фаз: ['Вимоги','Проєктування','Реалізація','Верифікація','Впровадження']
"""
from typing import List

PHASES = ['Вимоги', 'Проєктування', 'Реалізація', 'Верифікація', 'Впровадження']


def check_history(model: str, history: List[str]) -> str:
    if not isinstance(model, str) or not isinstance(history, list):
        raise ValueError("Некоректні дані")
    if any(not isinstance(x, str) for x in history):
        raise ValueError("Некоректні дані")

    # Map phase to index
    idx = {p: i for i, p in enumerate(PHASES)}

    backward_count = 0
    for i in range(1, len(history)):
        prev = history[i-1]
        curr = history[i]
        if prev not in idx or curr not in idx:
            # unknown phases — treat as invalid data
            raise ValueError("Некоректні дані")
        if idx[curr] < idx[prev]:
            # backward step
            if model == 'каскад':
                # report forbidden
                return f"Заборонений перехід: {prev} -> {curr} (крок {i})"
            elif model == "каскад зі зворотним зв'язком":
                backward_count += 1
            else:
                raise ValueError("Некоректні дані")
    # If no forbidden transitions
    if model == 'каскад':
        return f"Допустимо; кроків назад: 0"
    else:
        # model == 'каскад зі зворотним зв'язком'
        return f"Допустимо; кроків назад: {backward_count}"
