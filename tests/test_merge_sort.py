"""Tests for algos/merge_sort.py"""
from merge_sort import merge
from merge_sort import merge_sort

def test_merge():

    A = [99, 99, 2, 4, 5, 7, 1, 2, 3, 6, 99, 99]

    result = [99, 99, 1, 2, 2, 3, 4, 5, 6, 7, 99, 99]

    assert merge(A, 2, 5, 9) == result

def test_merge_sort():

    A = [5, 2, 4, 7, 1, 3, 2, 6]

    assert merge_sort(A, 0, len(A)-1) == [1, 2, 2, 3, 4, 5, 6, 7]