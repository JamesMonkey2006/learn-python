def long_division(n, d):
    """Print the qoutient and remainder of n and d
    Arguements:
    """
    q = n // d
    m = n % d
    print(n, 'divided by', d, 'equals', q, 'with remainder', m)


num = 12345
div = 6
long_division(num, div)
