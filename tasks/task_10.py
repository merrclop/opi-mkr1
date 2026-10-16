"""Task 10 — Gate для злиття PR (власники файлів)

Функція merge_gate(pr: dict, owners_rules: list[tuple[str,list[str]]]) -> list[str]
Повертає список повідомлень та висновок щодо можливості злиття.
Повідомлення і тексти — українською, точно у форматі тестів.
"""
from typing import Dict, List, Tuple


def _match_rule_for_file(fname: str, rules: List[Tuple[str, List[str]]]) -> List[str]:
    # Вибираємо найдовший збіг правила (найспецифічніше)
    best_rule = None
    best_len = -1
    best_owners: List[str] = []
    for pattern, owners in rules:
        if pattern == "*":
            L = 1
            matched = True
        else:
            matched = fname.startswith(pattern)
            L = len(pattern) if matched else -1
        if matched and L > best_len:
            best_len = L
            best_rule = pattern
            best_owners = owners
    return best_owners


def merge_gate(pr: Dict, owners_rules: List[Tuple[str, List[str]]]) -> List[str]:
    if not isinstance(pr, dict) or not isinstance(owners_rules, list):
        raise ValueError("Invalid PR data")

    files = pr.get("files")
    approvals = pr.get("approvals")

    if files is None or approvals is None:
        raise ValueError("Invalid PR data")

    if not isinstance(files, list) or not isinstance(approvals, list):
        raise ValueError("Invalid PR data")

    if len(files) == 0:
        raise ValueError("Немає змінених файлів")

    # normalize approvals
    app_set = set([a for a in approvals if isinstance(a, str)])

    reasons: List[str] = []

    # Перевірка по файлу та власникам
    for f in files:
        if not isinstance(f, str):
            raise ValueError("Invalid PR data")
        required = _match_rule_for_file(f, owners_rules)
        if required:
            # якщо жоден required не у approvals -> повідомлення
            ok = False
            for r in required:
                if r in app_set:
                    ok = True
                    break
            if not ok:
                reasons.append(f"Немає схвалення власників для: {f}")

    # Висновок
    if len(reasons) == 0:
        return ["Висновок: можна злити"]
    else:
        reasons.append("Висновок: не можна злити")
        return reasons
