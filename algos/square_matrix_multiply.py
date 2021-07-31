import numpy as np

def square_matrix_multiply(A, B):
    """
    Computes the square matrix C = A * B.

    Parameters
    ----------
    A : array-like of shape (n, n)
        Left matrix.
    B : array-like of shape (n, n)
        Right matrix.

    Returns
    -------
    C : array-like of shape (n, n)
        Product of A * B.
    """
    # Calculate shape of output matrix and create it with empty values.
    n = np.shape(A)[0]
    C = np.zeros((n, n))

    # Loop through each combination [i,j] to compute C[i,j].
    for i in range(n):
        for j in range(n):

            # Initialize C[i,j] to zero before we calculate the sum.
            C[i,j] = 0 

            # Calculate each term to be added to the sum.
            for k in range(n):
                C[i,j] += A[i,k] * B[k,j]

    return C

def square_matrix_recursive(A, B):
    """
    Computes the matrix C = A * B using recursion. 

    We assume n is an exact power of 2 if each of the n x n matrices.

    Parameters
    ----------
    A : numpy array of shape (n, n)
        Left matrix.
    B : numpy array of shape (n, n)
        Right matrix.

    Returns
    -------
    C : numpy array of shape (n, n)
        Product of A * B.
    """
    # Calculate shape of output matrix and create it with empty values.
    n = np.shape(A)[0]
    C = np.zeros((n, n))

    # Midpoint rounded down.
    mid = n // 2

    # Base case when A and B have one element we multiply them.
    if n == 1:
        C[0,0] = A[0,0] * B[0,0]
    
    # Split matrix into four square matrices and recursively multiply them.
    else:
        C[:mid,:mid] = square_matrix_recursive(A[:mid,:mid], B[:mid,:mid])\
                     + square_matrix_recursive(A[:mid,mid:], B[mid:,:mid])
        C[:mid,mid:] = square_matrix_recursive(A[:mid,:mid], B[:mid,mid:])\
                     + square_matrix_recursive(A[:mid,mid:], B[mid:,mid:])
        C[mid:,:mid] = square_matrix_recursive(A[mid:,:mid], B[:mid,:mid])\
                     + square_matrix_recursive(A[mid:,mid:], B[mid:,:mid])
        C[mid:,mid:] = square_matrix_recursive(A[mid:,:mid], B[:mid,mid:])\
                     + square_matrix_recursive(A[mid:,mid:], B[mid:,mid:])

    return C

def strassen_method(A, B):
    """
    Multiply two square matrices using Strassen's method.

    We assume n is an exact power of 2 if each of the n x n matrices.

    Parameters
    ----------
    A : array-like of shape (n, n)
        Left matrix.
    B : array-like of shape (n, n)
        Right matrix.

    Returns
    -------
    C : array-like of shape (n, n)
        Product of A * B.
    """
    # Calculate shape of output matrix and create it with empty values.
    n = np.shape(A)[0]
    C = np.zeros((n, n))

    # Midpoint rounded down.
    mid = n // 2

    # Base case when A and B have one element we multiply them.
    if n == 1:
        C[0,0]= A[0,0] * B[0,0]

    # Split matrices into 4 sub quadrants and solve with strassen's method.
    else:
        s1 = B[:mid,mid:] - B[mid:,mid:]
        s2 = A[:mid,:mid] + A[:mid,mid:]
        s3 = A[mid:,:mid] + A[mid:,mid:]
        s4 = B[mid:,:mid] - B[:mid,:mid]
        s5 = A[:mid,:mid] + A[mid:,mid:]
        s6 = B[:mid,:mid] + B[mid:,mid:]
        s7 = A[:mid,mid:] - A[mid:,mid:]
        s8 = B[mid:,:mid] + B[mid:,mid:]
        s9 = A[:mid,:mid] - A[mid:,:mid]
        s10 = B[:mid,:mid] + B[:mid,mid:]

        p1 = strassen_method(A[:mid,:mid], s1)
        p2 = strassen_method(s2, B[mid:,mid:])
        p3 = strassen_method(s3, B[:mid,:mid])
        p4 = strassen_method(A[mid:,mid:], s4)
        p5 = strassen_method(s5, s6)
        p6 = strassen_method(s7, s8)
        p7 = strassen_method(s9, s10)
        
        C[:mid,:mid] = p5 + p4 - p2 + p6 
        C[:mid,mid:] = p1 + p2
        C[mid:,:mid] = p3 + p4 
        C[mid:,mid:] = p5 + p1 - p3 - p7

    return C