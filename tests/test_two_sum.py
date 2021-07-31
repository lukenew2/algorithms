"""Tests for algos/two_sum.py"""

from two_sum import two_sum

def test_two_sum():

    S = {4, 9, 1, 2, 5, 8, 6}

    assert two_sum(S, 15) == True

    assert two_sum(S, 20) == False
