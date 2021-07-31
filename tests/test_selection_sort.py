"""Tests for algos/selection_sort.py."""

from selection_sort import selection_sort

def test_selection_sort():

    A = [31, 41, 59, 26, 41, 58]

    assert selection_sort(A) == [26, 31, 41, 41, 58, 59]