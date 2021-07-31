def bubble_sort(A):
    """
    Sort sequence of numbers by swapping adjacent elements out of order.

    Parameters
    ----------
    A : array-like of shape (n.)
        Sequence of numbers.
    
    Returns
    -------
    A : array-like of shape (n,)
        Sorted sequence of numbers.
    """
    # Loop through array ending at 2nd to last element.
    for i in range(len(A) - 1):

        # For each element loop backwards through array.
        for j in range(len(A) - 1, i, -1):

            # Check whether adjacent elements are out of order.
            if A[j] < A[j - 1]:

                # Swap elements.
                A[j], A[j - 1] = A[j - 1], A[j]

    return A