"""Tests for algos/linear_search.py."""

from algos.linear_search import linear_search

def test_linear_search():

    A = [31, 41, 59, 26, 41, 58]

    assert linear_search(A, 41) == 1

    assert linear_search(A, 2) == None