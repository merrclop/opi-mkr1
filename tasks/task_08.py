"""Task 08 — Триверсійне злиття (merge3)

Функція merge3(base, ours, theirs) -> str
Робить спрощене 3-way merge по рядках, як того очікують тести.
- якщо довжини різні — ValueError('Версії різної довжини')
- якщо тільки one side змінився — вибираємо зміну
- якщо обидва змінили і відрізняються — вставляємо конфліктні маркери
Повертаємо результат як текст, рядки розділені '\n'
"""
from typing import List


def merge3(base: List[str], ours: List[str], theirs: List[str]) -> str:
    if not (isinstance(base, list) and isinstance(ours, list) and isinstance(theirs, list)):
        raise ValueError('Версії різної довжини')
    if not (len(base) == len(ours) == len(theirs)):
        raise ValueError('Версії різної довжини')

    out_lines: List[str] = []
    for b, o, t in zip(base, ours, theirs):
        if o == t:
            # both same
            out_lines.append(o)
        else:
            if o == b and t != b:
                out_lines.append(t)
            elif t == b and o != b:
                out_lines.append(o)
            else:
                # both changed and differ -> conflict markers
                out_lines.append('<<<<<<< ours')
                out_lines.append(o)
                out_lines.append('=======')
                out_lines.append(t)
                out_lines.append('>>>>>>> theirs')
    return "\n".join(out_lines)
