import pytest
from fizz import *

def test_if_number_divided_by_3_returns_fizz():
    assert fizz_buzz(3) == 'fizz'

def test_if_number_divided_by_5_returns_buzz():
    assert fizz_buzz(5) == 'buzz'


def test_if_number_divided_by_3_and_5_returns_FizzBuzz():
    assert fizz_buzz(15) == 'FizzBuzz'