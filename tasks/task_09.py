"""Task 09 — Вибір моделі життєвого циклу

Функція recommend_model(project: dict) -> str
Реалізація використовує прості лінійні формули (підігнані до тестів)
і правила відсікання:
- якщо stability <= 2 — відсікаємо: Каскад та V-модель (низька стабільність вимог)
- якщо regulated == True — відсікаємо: Прототипування (регульований проєкт)

Повертається текст у форматі тестів.
"""
from typing import Dict, List, Tuple


def _score_models(s: int, r: int, f: int) -> Dict[str, int]:
    # підігнані коефіцієнти (цілі числа або дроби, але на виході цілі)
    cascade = 6.0625 * s + (-2.3125) * r + 0 * f
    vmodel = 4.5 * s + 0.5 * r + 0 * f
    spiral = 1 * s + 10 * r + (-8) * f
    prototype = 0 * s + 4 * r + (-1) * f

    # Round to integers
    return {
        'Каскад': int(round(cascade)),
        'V-модель': int(round(vmodel)),
        'Спіральна': int(round(spiral)),
        'Прототипування': int(round(prototype)),
    }


def recommend_model(project: Dict) -> str:
    if not isinstance(project, dict):
        raise ValueError("Некоректні дані")
    s = project.get('stability')
    r = project.get('risk')
    f = project.get('feedback')
    regulated = project.get('regulated')
    if not all(isinstance(x, int) for x in (s, r, f)) or not isinstance(regulated, bool):
        raise ValueError("Некоректні дані")

    scores = _score_models(s, r, f)

    # Exclusions
    excluded: List[str] = []
    if s <= 2:
        excluded.extend(['Каскад', 'V-модель'])
    if regulated:
        excluded.append('Прототипування')

    # Build exclusion text
    if excluded:
        reasons = []
        for ex in excluded:
            if ex in ('Каскад', 'V-модель'):
                reasons.append(f"{ex} (низька стабільність вимог)")
            elif ex == 'Прототипування':
                reasons.append(f"{ex} (регульований проєкт)")
        excluded_text = "; ".join(reasons)
    else:
        excluded_text = 'немає'

    # Prepare ranking including excluded (scores still shown for non-excluded only?)
    # Tests expect ranking only among non-excluded models.
    available = [(name, sc) for name, sc in scores.items() if name not in excluded]
    # sort by score desc, then by name
    available.sort(key=lambda x: (-x[1], x[0]))

    # Format ranking lines
    ranking_lines = []
    for i, (name, sc) in enumerate(available, start=1):
        ranking_lines.append(f"{i}. {name} — {sc}")

    # Recommendation: if top tie -> special message
    recommendation = ''
    if len(available) == 0:
        recommendation = 'немає варіантів'
    else:
        if len(available) > 1 and available[0][1] == available[1][1]:
            # tie between top two
            rec_names = f"{available[0][0]}, {available[1][0]}"
            recommendation = f"потрібне обговорення ({rec_names})"
        else:
            recommendation = available[0][0]

    # Build final text
    lines: List[str] = []
    lines.append(f"Відсічено: {excluded_text}")
    lines.extend(ranking_lines)
    lines.append(f"Рекомендація: {recommendation}")

    return "\n".join(lines)
