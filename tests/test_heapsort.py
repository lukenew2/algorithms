from algos.heapsort import heapsort

def test_heapsort():

    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

    heapsort(A)

    assert A == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]