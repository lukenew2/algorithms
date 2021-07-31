"""Module containing tests for algos/inversions.py."""

from inversions import inversions
from inversions import merge_sort_inversions

def test_inversions():

    A = [2, 3, 8, 6, 1]

    assert inversions(A) == 5

