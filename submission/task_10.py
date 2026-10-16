"""Task 10 — Merge gate (submission copy)

Копія реалізації для здачі: merge_gate(pr, owners_rules)
"""
from typing import Dict, List, Tuple


def _match_rule_for_file(fname: str, rules: List[Tuple[str, List[str]]]) -> List[str]:
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

    app_set = set([a for a in approvals if isinstance(a, str)])

    reasons: List[str] = []

    for f in files:
        if not isinstance(f, str):
            raise ValueError("Invalid PR data")
        required = _match_rule_for_file(f, owners_rules)
        if required:
            ok = False
            for r in required:
                if r in app_set:
                    ok = True
                    break
            if not ok:
                reasons.append(f"Немає схвалення власників для: {f}")

    if len(reasons) == 0:
        return ["Висновок: можна злити"]
    else:
        reasons.append("Висновок: не можна злити")
        return reasons
