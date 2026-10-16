"""Відкриті приклади 10 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(10)

PUBLIC = [('merge_gate',
  ({'author': 'olena',
    'files': ['src/app.py', 'docs/guide.md'],
    'lines_changed': 120,
    'ci': 'pass',
    'approvals': ['petro', 'iryna'],
    'comments': [('Пропозиція', False), ('Блокер', True)]},
   [('*', ['petro']), ('docs/', ['iryna'])]),
  ['Висновок: можна злити']),
 ('merge_gate',
  ({'author': 'olena',
    'files': ['src/app.py', 'docs/guide.md'],
    'lines_changed': 120,
    'ci': 'pass',
    'approvals': ['petro'],
    'comments': [('Пропозиція', False), ('Блокер', True)]},
   [('*', ['petro']), ('docs/', ['iryna'])]),
  ['Немає схвалення власників для: docs/guide.md', 'Висновок: не можна злити']),
 ('merge_gate',
  ({'author': 'olena',
    'files': [],
    'lines_changed': 120,
    'ci': 'pass',
    'approvals': ['petro', 'iryna'],
    'comments': [('Пропозиція', False), ('Блокер', True)]},
   [('*', ['petro']), ('docs/', ['iryna'])]),
  ('ValueError', 'Немає змінених файлів'))]


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
    for name in ('merge_gate',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
