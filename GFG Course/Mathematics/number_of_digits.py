# Given a number count the number of digits in it
import math
def count_digits(n):
    return 1 + math.floor(math.log10(n))

print(count_digits(5000))