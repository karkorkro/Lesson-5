import pytest
from bank_account import *


@pytest.mark.parametrize('balance, price, expected_result',
                         [(1000, 200, 800.0), (150, 15.5, 134.5), (200, 1000, False)])
def test_charging(balance, price, expected_result):
    assert charging(balance, price) == expected_result
