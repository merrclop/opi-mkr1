"""Відкриті приклади 06 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(6)

PUBLIC = [('audit_requirements',
  (['flask==2.0.1', 'requests>=2.0', 'jinja2==3.1.4'],
   {'flask': [('CVE-A', '2.2.5')], 'jinja2': [('CVE-B', '3.1.3')]}),
  ['flask 2.0.1: вразливість CVE-A, виправлено у 2.2.5', 'Версію не зафіксовано: requests']),
 ('audit_requirements', (['Flask==3.0.0'], {'flask': [('X', '3.0.0')]}), []),
 ('audit_requirements',
  (['flask==1.0', 'flask==2.0'], {}),
  ('ValueError', 'Дублікат пакета: flask'))]


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
    for name in ('audit_requirements',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
