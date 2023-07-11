import pytest
from sort import *

def test_if_returns_sorted_list():
    tab = [1, 3, 2, 6, 5]
    assert quickSort(tab, 0, len(tab)-1) == sorted(tab)

