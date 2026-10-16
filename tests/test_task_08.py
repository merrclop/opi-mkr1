"""Відкриті приклади 08 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(8)

PUBLIC = [('merge3', (['a', 'b', 'c'], ['a', 'B', 'c'], ['a', 'b', 'C']), 'a\nB\nC'),
 ('merge3',
  (['a', 'b', 'c'], ['a', 'X', 'c'], ['a', 'Y', 'c']),
  'a\n<<<<<<< ours\nX\n=======\nY\n>>>>>>> theirs\nc'),
 ('merge3', (['a'], ['a', 'b'], ['a']), ('ValueError', 'Версії різної довжини'))]


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
    for name in ('merge3',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
