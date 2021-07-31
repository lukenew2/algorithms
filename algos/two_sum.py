def two_sum(S, x):
    """
    Given set of n integers and another integer x, determines where or not 
    there exist two elements in A whose sum is exactly x.

    Parameters
    ----------
    S : Set of shape (n,)
        Sequence of n unique elements.
    x : int
        Target value to check if two elements exist in A whose sum is x.
    
    Returns
    -------
    True/False : Boolean
        True if condition is met, else False.
    """
    # Empty set to hold target matches.
    B = set()

    # Loop through each number in given set S.
    for num in S:

        # Check if number is a match of previous number.
        if num in B:
            return True
        
        # Add the number's match to our set.
        B.add(x - num)
    
    # Target condition not met.
    return False