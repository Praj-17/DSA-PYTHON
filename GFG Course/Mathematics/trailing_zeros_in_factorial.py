def trailing_zeros_in_factorial(n):
    """
    floor(n/5) + floor(n/25) + floor(n/125)
    """
    count = 0
    i = 5
    while (n / i>= 1):
        count += int(n / i)
        i *= 5

    return int(count)