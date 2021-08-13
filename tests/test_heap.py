"""Module containing tests for ./algos/heap.py"""
from algos.heap import Heap

def test_parent():
    
    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    max_heap = Heap(A)

    assert max_heap.parent(3) == 1
    assert max_heap.parent(4) == 1

def test_left():

    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    max_heap = Heap(A)

    assert max_heap.left(3) == 7
    assert max_heap.left(4) == 9

def test_right():

    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    max_heap = Heap(A)

    assert max_heap.right(2) == 6
    assert max_heap.right(3) == 8

def test_max_heapify():

    A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

    heap = Heap(A) 

    heap.max_heapify(A, 1)

    assert A == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] 