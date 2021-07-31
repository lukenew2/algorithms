def insertion_sort(A, asc=True):
    """
    Insertion sorting algorithm for sequence of n numbers.

    Parameters
    ------
    A : array-like of shape (n,)
        Array to be sorted.
    asc : boolean
        If True sorts sequence in increasing order.

    Returns
    -------
    A : array-like of shape (n,)
    Sorted array.

    Notes
    -----
    This algorithm sorts the array in place without creating a new array.
    """
    # Loop through array starting at 2nd element.
    for j in range(1, len(A)):

        # Assign current element and index of previous element to variables.
        key = A[j]
        i = j - 1

        # Insert element A[j] in increasing order.
        if asc:
            while i > -1 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key
            
        # Insert element A[j] in decreasing order
        else:
            while i > -1 and A[i] < key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key

    return A