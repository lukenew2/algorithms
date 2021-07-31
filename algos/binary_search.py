def binary_search(A, v, p, r):
    """
    Scan sorted sequence of numbers looking for the index where v appears.

    Parameters
    ----------
    A : array-like of shape (n,)
        Sorted sequence of n numbers in increasing order.
    p : int
        Index representing start of sequence.
    r : int
        Index representing end of sequence.
    v : int
        Integer value to be scanned for in array.

    Returns
    -------
    i : int
        First index such that v = A[i] or NULL if v does not appear.
    """

    # Only binary search if there is more than one element.
    if p < r:

        # Find midpoint rounded down.
        midpoint = p + (r - p) // 2

        # Return index if value matches midpoint.
        if v == A[midpoint]:
            return midpoint

        # Search bottom half if value is less than the midpoint.
        elif v < A[midpoint]:
            return binary_search(A, v, p, midpoint - 1)

        # Search top half if the value is greater than the midpoint.
        elif v > A[midpoint]:
            return binary_search(A, v, midpoint + 1, r)

    else:

        # Check if element is target value.
        if v == A[p]:
            return p

        # Value not in array.
        else:
            return None
    
