"""Tests for algos/binary_search.py."""
from algos.binary_search import binary_search

def test_binary_search():

    A = [0, 3, 4, 7, 9, 10, 11, 15]

    B = [0, 3, 4, 7, 9, 10, 11]

    assert binary_search(A, 0, 0, len(A)-1) == 0

    assert binary_search(B, 11, 0, len(B)-1) == 6

    assert binary_search(A, 2, 0, len(A)-1) == None

    assert binary_search(B, 2, 0, len(B)-1) == None