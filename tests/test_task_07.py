"""Відкриті приклади 07 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(7)

PUBLIC = [('branch_status',
  ({'A': [],
    'B': ['A'],
    'C': ['B'],
    'D': ['B'],
    'E': ['D'],
    'F': ['C'],
    'G': ['F'],
    'P': ['C', 'D'],
    'Q': ['D', 'C']},
   'C',
   'E'),
  'Спільний предок: B\nВипереджає: 2\nВідстає: 1\nЗлиття: потрібен merge-коміт'),
 ('branch_status',
  ({'A': [],
    'B': ['A'],
    'C': ['B'],
    'D': ['B'],
    'E': ['D'],
    'F': ['C'],
    'G': ['F'],
    'P': ['C', 'D'],
    'Q': ['D', 'C']},
   'C',
   'G'),
  'Спільний предок: C\nВипереджає: 2\nВідстає: 0\nЗлиття: fast-forward'),
 ('branch_status',
  ({'A': [],
    'B': ['A'],
    'C': ['B'],
    'D': ['B'],
    'E': ['D'],
    'F': ['C'],
    'G': ['F'],
    'P': ['C', 'D'],
    'Q': ['D', 'C']},
   'P',
   'Z'),
  ('ValueError', 'Невідомий коміт: Z'))]


def _call(fn, args):
    return getattr(M, fn)(*copy.deepcopy(args))


def _check(fn, args, expected):
    if isinstance(expected, tuple) and expected and expected[0] == "ValueError":
        with pytest.raises(ValueError) as info:
            _call(fn, args)
        assert str(info.value) == expected[1]
    else:
        assert _call(fn, args) == expected


@pytest.mark.parametrize("fn,args,expected", PUBLIC, ids=[f"p{i}" for i in range(len(PUBLIC))])
def test_public(fn, args, expected):
    _check(fn, args, expected)


def test_functions_exist():
    for name in ('branch_status',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
