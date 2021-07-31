"""Tests for algos/square_matrix_multiply.py"""

import numpy as np
from numpy.testing import assert_array_equal
from algos.square_matrix_multiply import square_matrix_multiply
from algos.square_matrix_multiply import square_matrix_recursive
from algos.square_matrix_multiply import strassen_method


def test_square_matrix_multiply():
    
    A = np.array([[2, 1],
                  [1, 2]])

    B = np.array([[0, 1],
                  [1, 2]])

    C = np.array([[1, 4],
                  [2, 5]])

    assert_array_equal(square_matrix_multiply(A, B), C)
    assert_array_equal(square_matrix_recursive(A, B), C)
    assert_array_equal(strassen_method(A, B), C)
