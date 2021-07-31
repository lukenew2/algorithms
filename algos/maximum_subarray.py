import numpy as np

def find_max_crossing_subarray(A, low, mid, high):
    """
    Finds maximum subarray that goes through midpoint of an array.

    Parameters
    ----------
    A : array-like of shape (n,)
        Sequence of n numbers.
    low : int
        Starting index of left subarray.
    mid : int
        Index representing midpoint of array.
    high : int
        Last index of right subarray.

    Returns
    -------
    (max-left, max-right, left-sum + right-sum) : tuple
        Tuple containing the indices demarcating a maximum subarray that
        crosses the midpoint.
    """
    # Holds greatest sum found so far in left subarray.
    left_sum = -np.inf

    # Holds sum of entries found in A[i .. mid].
    sum = 0

    # Loop from midpoint down to lowest index for left subarray.
    for i in range(mid, low - 1, -1):
        
        # Calculate current sum.
        sum += A[i]

        # Check if current sum is greater than greatest sum found so far.
        if sum > left_sum:

            # Set greatest sum to current sum and store the left index.
            left_sum = sum
            max_left = i

    # Holds greatest sum found so far in right subarray.
    right_sum = -np.inf

    # Holds sum of entries found in A[mid + 1 .. j]
    sum = 0

    # Loop from midpoint + 1 up to end of right subarray.
    for j in range(mid + 1, high + 1):

        # Calculate current sum.
        sum += A[j]

        # Check if current sum is greater than greatest sum found so far.
        if sum > right_sum:

            # Set greatest sum to current sum and store the right index.
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    """
    Recursively finds maximum subarray in sequence of numbers.

    Parameters
    ----------
    A : array-like of shape (n,)
        Sequence of n numbers.
    low : int
        Index representing beginning of sequence.
    high : int
        Index representing end of sequence.

    Returns
    -------
    (low, high, sum) : tuple
        Tuple containing start and end of maximum subarray and the sum.
    """
    # If sequence contains one element maximum subarray is that element.
    if low == high:
        return (low, high, A[low])

    # Divide sequence into two subproblems.
    else:

        # Calculate midpoint rounded down.
        mid = low + (high - low) // 2

        # Recursively solve left subarray.
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)

        # Recursively solve right subarray.
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1,
                                                                   high)

        # Find max subarray that crosses the midpoint.
        (cross_left, cross_right, cross_sum) = find_max_crossing_subarray(A, 
                                                                          low, 
                                                                          mid, 
                                                                          high)
        
        # Check if max left subarray is larger than right and cross.
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)

        # Check if max right subarray is larger than left and cross.
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        
        # Check if subarray crossing midpoint is larger than left and right.
        elif cross_sum >= left_sum and cross_sum >= right_sum:
            return (cross_left, cross_right, cross_sum)

def find_max_subarray_brute_force(A):
    """
    Find maximum subarray using brute force method.

    Parameters
    ----------
    A : array-like of shape (n,)
        Sequence of n numbers.

    Returns
    -------
    (left, right, greatest_sum): tuple
        Tuple containing the indices of start, end, and sum of max subarray.
    """
    # Holds gretest sum, starting index, and ending index of max subarray.
    greatest_sum = -np.inf
    left = 0
    right = len(A)

    # Loop through each element.
    for i in range(len(A)):

        # Set current sum equal to the single element.
        sum = A[i]

        # Check if this element is greater than the greatest sum found so far.
        if sum > greatest_sum:

            # Set the greatest sum equal to the current sum.
            greatest_sum = sum 

            # Set the indices of left and right to the element's index.
            left = i
            right = i 
        
        # For each element loop through all the elements that follow.
        for j in range(i + 1, len(A)):

            # Increment current sum.
            sum += A[j]

            # Check if sum of sequence A[i .. j] is larger than greatest sum.
            if sum > greatest_sum:

                # Set greatest sum equal to the current sum.
                greatest_sum = sum

                # Set indices of left and right to start and end of subarray.
                left = i 
                right = j

    return (left, right, greatest_sum)

def find_maximum_subarray_nonrecursive(A):
    """
    Find maximum subarray using a nonrecursive linear-time algorithm.

    Parameters
    ----------
    A : array-like of shape (n,)
        Sequence of n numbers.

    Returns
    -------
    (left, right, greatest_sum): tuple
        Tuple containing the indices of start, end, and sum of max subarray.    
    """
    # Define variables for max subarray ending at index i and max seen so far.
    max_so_far = -np.inf
    max_ending_here = A[0]

    # Loop through array starting at second element to the end.
    for i in range(1, len(A)):

        # Take the max between element at index i and previous contiguous array.
        max_ending_here = max(max_ending_here + A[i], A[i])

        # Update max subarray seen so far.
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
    


            