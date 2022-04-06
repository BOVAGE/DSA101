def factorial(n):
    """
        returns the factorial of n. (n!)
    """
    if n < 0:
        return 'n must be a non-negative integer'
    elif n == 0:
        return 1
    return n * factorial(n-1)
