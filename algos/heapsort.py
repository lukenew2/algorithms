from algos.heap import Heap 

def heapsort(A):
    """
    Sort array inplace using heapsort algorithm.

    Parameters
    ----------
    A : array-like of shape (n,)
        Unordered array.
    """
    # Instantiate heap
    heap = Heap(A)

    # Build max heap
    heap.build_max_heap(A)
    
    # Exchange root node with element i.
    for i in range(heap.heapsize, 0, -1):
        A[0], A[i] = A[i], A[0]

        # Discard node i and restore max heap property for node 0.
        heap.heapsize -= 1
        heap.max_heapify(A, 0)