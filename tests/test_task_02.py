"""Відкриті приклади 02 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(2)

PUBLIC = [('check_history',
  ('каскад', ['Вимоги', 'Проєктування', 'Реалізація']),
  'Допустимо; кроків назад: 0'),
 ('check_history',
  ("каскад зі зворотним зв'язком",
   ['Вимоги',
    'Проєктування',
    'Реалізація',
    'Верифікація',
    'Реалізація',
    'Верифікація',
    'Впровадження']),
  'Допустимо; кроків назад: 1'),
 ('check_history',
  ('каскад', ['Вимоги', 'Проєктування', 'Реалізація', 'Верифікація', 'Реалізація']),
  'Заборонений перехід: Верифікація -> Реалізація (крок 4)')]


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
    for name in ('check_history',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
