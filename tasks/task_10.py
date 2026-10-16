"""Task 10 — Готовність PR до злиття (merge gate)

Функція merge_gate(pr: dict, required_approvals: int = 1) -> (bool, list[str])
Приймає словник з метаданими PR і повертає кортеж (is_ready, reasons).
Очікувані поля в pr:
- ci_passed: bool
- has_conflicts: bool
- approvals: int
- mergeable: bool (опціонально)
- failing_checks: list (опціонально)

Валідація: на некоректні дані кидає ValueError("Invalid PR data").
"""
from typing import Dict, List, Tuple


def merge_gate(pr: Dict, required_approvals: int = 1) -> Tuple[bool, List[str]]:
    if not isinstance(pr, dict) or not isinstance(required_approvals, int):
        raise ValueError("Invalid PR data")

    # Required keys and types
    ci_passed = pr.get("ci_passed")
    has_conflicts = pr.get("has_conflicts")
    approvals = pr.get("approvals")

    if not isinstance(ci_passed, bool) or not isinstance(has_conflicts, bool) or not isinstance(approvals, int):
        raise ValueError("Invalid PR data")

    reasons: List[str] = []

    if not ci_passed:
        reasons.append("CI not passed")

    if has_conflicts:
        reasons.append("Has merge conflicts")

    if approvals < required_approvals:
        reasons.append("Not enough approvals")

    failing_checks = pr.get("failing_checks")
    if failing_checks is not None:
        if not isinstance(failing_checks, list):
            raise ValueError("Invalid PR data")
        if len(failing_checks) > 0:
            reasons.append("Failing checks: " + ", ".join(map(str, failing_checks)))

    mergeable = pr.get("mergeable")
    if mergeable is not None and not isinstance(mergeable, bool):
        raise ValueError("Invalid PR data")
    if mergeable is False:
        reasons.append("Not mergeable")

    is_ready = len(reasons) == 0
    return is_ready, reasons
