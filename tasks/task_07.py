"""Task 07 — Стан гілок в історії комітів

Функція branch_status(parents: dict[str,list[str]], main: str, feature: str) -> str
Повертає звіт у форматі тестів:
Спільний предок: {commit}\nВипереджає: {n1}\nВідстає: {n2}\nЗлиття: {fast-forward|потрібен merge-коміт}

Якщо commit не відомий — кидає ValueError('Невідомий коміт: {name}')
"""
from typing import Dict, List
from collections import deque


def _distances_to_ancestors(parents: Dict[str, List[str]], node: str):
    # BFS upward: node -> parents -> ... record distance (steps) to each ancestor including itself (0)
    q = deque()
    q.append((node, 0))
    d = {}
    while q:
        cur, dist = q.popleft()
        if cur in d:
            continue
        d[cur] = dist
        for p in parents.get(cur, []):
            q.append((p, dist+1))
    return d


def branch_status(parents: Dict[str, List[str]], main: str, feature: str) -> str:
    if main not in parents:
        raise ValueError(f"Невідомий коміт: {main}")
    if feature not in parents:
        raise ValueError(f"Невідомий коміт: {feature}")

    dm = _distances_to_ancestors(parents, main)
    df = _distances_to_ancestors(parents, feature)

    # common ancestors
    commons = set(dm.keys()) & set(df.keys())
    if not commons:
        # shouldn't happen with given tests
        common = None
    else:
        # choose ancestor with minimal total distance (dm+df)
        best = None
        best_sum = None
        for c in commons:
            s = dm[c] + df[c]
            if best is None or s < best_sum:
                best = c
                best_sum = s
        common = best

    ahead = df.get(common, 0)
    behind = dm.get(common, 0)

    if behind == 0:
        merge_type = 'fast-forward'
    else:
        if ahead == 0:
            merge_type = 'fast-forward'
        else:
            merge_type = 'потрібен merge-коміт'

    return (
        f"Спільний предок: {common}\n"
        f"Випереджає: {ahead}\n"
        f"Відстає: {behind}\n"
        f"Злиття: {merge_type}"
    )
