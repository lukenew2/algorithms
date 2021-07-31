def selection_sort(A):
    """
    Sort sequence of n numbers by selection sort algorithm.

    Parameters
    ----------
    A : array-like of shape (n,)
        Target array to be sorted.

    Returns
    -------
    A : array-like of shape (n,)
        Sorted array.
    """
    # Assign key determining where to start each search for the min.
    j = 0

    # Search for min n - 1 times.
    while j < len(A):

        # Placeholder storing index of min found in below loop.
        min_index = -1

        # Search for smallest value and assign its index to variable.
        for index, value in enumerate(A[j:], start=j):
            if value < A[min_index]:
                min_index = index
            
        # Exchange values. 
        A[j], A[min_index] = A[min_index], A[j]

        # Increment key.
        j += 1

    return A

