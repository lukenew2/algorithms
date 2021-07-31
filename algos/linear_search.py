def linear_search(A, v):
    """
    Scans through sequence looking for the index where the value v appears.

    Parameters
    ----------
    A : array-like of shape (n,)
    Sequence of n numbers.
    v : int
    Integer value to be scanned for in array.

    Returns
    -------
    i : int
    First index such that v = A[i] or NULL if v does not appear.
    """
    for index, value in enumerate(A):
        if v == value:
            return index
        
    return None