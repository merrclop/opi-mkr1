"""Відкриті приклади 03 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(3)

PUBLIC = [('secrets_report',
  (['DB_HOST=localhost', 'DB_PASSWORD=hunter2', 'API_TOKEN="abc123"'],),
  ['Рядок 2: можливий секрет у «DB_PASSWORD»', 'Рядок 3: можливий секрет у «API_TOKEN»']),
 ('secrets_report',
  (['# password=1234', 'DB_PASSWORD=${DB_PASSWORD}', 'token = os.environ["TOKEN"]'],),
  []),
 ('secrets_report', ([1],), ('ValueError', 'Некоректні дані'))]


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
    for name in ('secrets_report',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
