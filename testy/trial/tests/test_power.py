from functionality.operations import *


def test_should_return_correct_value_for_positive_exp():
    base = 5
    exp = 3

    assert calc_power(base, exp) == 125


def test_should_return_1_for_0_exp():
    base1 = 5
    base2 = 10
    exp = 0

    assert calc_power(base1, exp) == 1
    assert calc_power(base2, exp) == 1
