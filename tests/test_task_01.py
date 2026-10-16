"""Відкриті приклади 01 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(1)

PUBLIC = [('crisis_signs',
  (100, 150, 20, 30, 6, 10),
  'Ознак кризи: 3\n'
  'Ознаки: Перевищено бюджет; Зірвано строки; Недопоставлено функції\n'
  'Висновок: криза проєкту'),
 ('crisis_signs',
  (100, 120, 20, 24, 9, 10),
  'Ознак кризи: 0\nОзнаки: немає\nВисновок: проєкт у нормі'),
 ('crisis_signs', (0, 120, 20, 24, 9, 10), ('ValueError', 'Некоректні дані'))]


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
    for name in ('crisis_signs',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
