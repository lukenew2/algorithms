def complex_multiply(a, b, c, d):
    """
    Multiply two complex numbers using three multiplcations.

    Parameters
    ----------
    a : float
        Variable a in first imaginary number a + bi.
    b : float
        Variable b in first imaginary number a + bi.
    c : float
        Variable c in second imaginary number c + di.
    d : float
        Variable d in second imaginary number c + di.

    Returns
    -------
    Real : float
        Real componenet ac - bd.
    Imaginary : float
        Imaginary componenet ad + bc.
    """
    # Three intermediary products.
    p1 = a * c 
    p2 = b * d 
    p3 = (a + b) * (c + d)

    # Real and Imaginary components.
    real = p1 - p2 
    imaginary = p3 - p2 - p1 

    return (real, imaginary)

