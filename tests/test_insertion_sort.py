"""Tests for algos/insertion_sort.py."""
from algos.insertion_sort import insertion_sort


def test_insertion_sort():

    A = [31, 41, 59, 26, 41, 58]

    assert insertion_sort(A) == [26, 31, 41, 41, 58, 59]

    assert insertion_sort(A, asc=False) == [59, 58, 41, 41, 31, 26]

