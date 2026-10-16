"""Відкриті приклади 09 (з картки). Повний набір перевірок — у викладача."""
import copy

import pytest
from conftest import load

M = load(9)

PUBLIC = [('recommend_model',
  ({'stability': 2, 'risk': 5, 'feedback': 3, 'regulated': False},),
  'Відсічено: Каскад (низька стабільність вимог); V-модель (низька стабільність вимог)\n'
  '1. Спіральна — 28\n'
  '2. Прототипування — 17\n'
  'Рекомендація: Спіральна'),
 ('recommend_model',
  ({'stability': 5, 'risk': 1, 'feedback': 1, 'regulated': True},),
  'Відсічено: Прототипування (регульований проєкт)\n'
  '1. Каскад — 28\n'
  '2. V-модель — 23\n'
  '3. Спіральна — 7\n'
  'Рекомендація: Каскад'),
 ('recommend_model',
  ({'stability': 4, 'risk': 4, 'feedback': 3, 'regulated': False},),
  'Відсічено: немає\n'
  '1. V-модель — 20\n'
  '2. Спіральна — 20\n'
  '3. Каскад — 15\n'
  '4. Прототипування — 13\n'
  'Рекомендація: потрібне обговорення (V-модель, Спіральна)')]


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
    for name in ('recommend_model',):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
