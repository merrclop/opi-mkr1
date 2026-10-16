"""Відкриті приклади 04 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(4)

PUBLIC = [('next_version', ('1.4.2', ['fix: виправлено збій', 'docs: оновлено README']), '1.4.3'),
 ('next_version', ('1.4.2', ['feat(api): нова кінцева точка', 'fix: дрібне виправлення']), '1.5.0'),
 ('next_version',
  ('1.4.2', ['Виправлено збій']),
  ('ValueError', 'Некоректне повідомлення: Виправлено збій'))]


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
    for name in ('next_version',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
