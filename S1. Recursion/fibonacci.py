def fib(n):
    """
        returns the nth term in fibonacci sequence
    """
    if n < 1:
        return "Domain must be a postive integer"
    elif n == 1 or n == 2:
        return n - 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(8))