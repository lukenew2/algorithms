def inversions(A):
    """
    Count number of inversions in given array.

    Number of inversions are used to determine how out of order an array is.  
    For any indices i < j, if A[i] > A[j], then the pair (i,j) is an inversion.

    Parameters
    ----------
    A : array-like of shape (n,)
        Array to count inversions.

    Returns
    -------
    C : int
        Number of inversions.
    """
    # Initiate inversion count at 0.
    count = 0

    # Loop through array up to 2nd to last element. 
    for i in range(len(A) - 1):

        # For each element, loop through the following element to end of array.
        for j in range(i + 1, len(A)):
            
            # Check if pair (i,j) is an inversion.
            if A[i] > A[j]:
                
                # Increment inversion count.
                count += 1

    return count

def merge_inversions(A, p, q, r):
    """
    Counts number of inversions in two sorted subarrays A[p:q] and A[q+1:r]
    and merges them.

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
    C : int
        Number of inversions.
    A : array-like of shape (n,)
        Merged sorted array.
    """
    # Create two subarrays to be merged.
    L = A[p:q+1]
    R = A[q+1:r+1]

    # Indices representing current index of each array.
    i, j = 0, 0

    # Initiate inversion count at 0.
    count = 0

    # Loop for each element in the initial subarray.
    for index in range(p, r+1):

        # Replace value of initial array with value from left subarray.
        if L[i] <= R[j]:
            A[index] = L[i]
            i += 1

            # If left array runs out assign the remaining values of right array.
            if i == len(L):
                A[index+1:r+1] = R[j:]

                return A, count
        
        # Replace value of initial array with value from right subarray.
        elif L[i] > R[j]:
            A[index] = R[j]
            j +=1 

            # Increment inversions by (midpoint - i).
            count += (q + 1 - i)

            # If right array runs out assign the remaining values of left array.
            if j == len(R):
                A[index+1:r+1] = L[i:]

                return A, count

    return A, count

def merge_sort_inversions(A, p, r):
    """
    Count number of inversions in number sequence with merge sort algorithm.

    Divides sequence into two subsequences and recursively sorting the
    subsequences and counting the number of inversions in each subarray.

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
    C : int
        Number of inversions.
    """
    # Initiate inversion count at 0.
    count = 0

    # If p >=r the array has at most 1 element and therefore is already sorted.
    if p < r:

        # Middle of sequence rounded down.
        q = p + (r - p) // 2

        # Count number of inversions in each subarray.
        A, inversions = merge_sort_inversions(A, p, q)
        count += inversions

        A, inversions = merge_sort_inversions(A, q+1, r)
        count += inversions

        # Merge two sorted subarrays and increment count of inversions in merge.
        A, inversions = merge_inversions(A, p, q, r)
        count += inversions

    return A, count



