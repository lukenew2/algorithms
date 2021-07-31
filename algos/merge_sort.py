def merge(A, p, q, r):
    """
    Combines two sorted subarrays A[p:q] and A[q+1:r] in sorted array.

    Parameters
    ----------
    A : array-like of shape (n,)
        Array containing two subarrays to be merged.
    p : int
        Starting index of first subarray.
    q : int
        Ending index of first subarray.
    r : int
        Ending index of second subarray.

    Returns
    -------
    A : array-like of shape (n,)
        Merged sorted array.
    """
    # Create two subarrays to be merged.
    L = A[p:q+1]
    R = A[q+1:r+1]

    # Indices representing current index of each array.
    i, j = 0, 0

    # Loop for each element in the intial subarray.
    for index in range(p, r+1):

        # Replace value of initial array with value from left subarray.
        if L[i] <= R[j]:
            A[index] = L[i]
            i += 1

            # If left array runs out assign the remaining values of right array.
            if i == len(L):
                A[index+1:r+1] = R[j:]

                return A

        # Replace value of initial array with value from right subarray.
        elif L[i] > R[j]:
            A[index] = R[j]
            j += 1

            # If right array runs out assign the remaining values of left array.
            if j == len(R):
                A[index+1:r+1] = L[i:]

                return A

    return A

def merge_sort(A, p, r):
    """
    Sort number sequence with merge sort algorithm.

    Divides sequence into two subsequences and recursively sorts the
    subsequences by merging sorted subsequences to produce the sorted answer.

    Parameters
    ----------
    A : array-like of shape (n,)
        Sequence of numbers to be sorted.
    p : int
        Index representing start of sequence.
    r : int
        Index representing end of sequence.

    Returns
    -------
    A : array-like of shape (n,)
        Sorted sequence of numbers.
    """
    # If p >=r the array has at most 1 element and therefore is already sorted.
    if p < r:

        # Middle of sequence rounded down.
        q = p + (r - p) // 2

        # Merge sort subsequences recursively.
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)

        # Merge sorted subsequences to produce sorted sequence.
        merge(A, p, q, r)

    return A