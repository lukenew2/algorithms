"""Tests for algos/bubble_sort.py."""
from bubble_sort import bubble_sort


def test_bubble_sort():

    A = [31, 41, 59, 26, 41, 58]

    assert bubble_sort(A) == [26, 31, 41, 41, 58, 59]