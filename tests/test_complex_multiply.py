"""Tests for algos/complex_multiply.py"""

from complex_multiply import complex_multiply

def test_complex_multiply():

    a, b, c, d = 1, 2, 3, 4 

    assert complex_multiply(a, b, c, d) == (-5, 10)