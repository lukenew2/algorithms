"""Tests for algos/maximum_subarray.py"""

from algos.maximum_subarray import find_maximum_subarray
from algos.maximum_subarray import find_max_subarray_brute_force
from algos.maximum_subarray import find_maximum_subarray_nonrecursive

def test_find_maximum_subarray():

    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    assert find_maximum_subarray(A, 0, len(A)-1) == (7, 10, 43)

    assert find_max_subarray_brute_force(A) == (7, 10, 43)

    assert find_maximum_subarray_nonrecursive(A) == (43)