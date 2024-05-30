import math
def count_digits_in_fact(n):
    """
    Intuition:
    1. number of digits = 1 + floor(log10(n))
    2. Log(x*y) = log(x) + log(y)
    # ans = 1 + math.floor(math.log10(n!))
     ans = 1 + math.floor(math.log10(1*2*3*...n))
     ans = 1 + math.floor(math.log10(1) +math.log10(2) + math.log10(3) + ... math.log10(n) )
     sum = math.log10(1) +math.log10(2) + math.log10(3) + ... math.log10(n)
    
    """
    return 1 + math.floor(sum([math.log10(i) for i in range(1,n+1)]))

print(count_digits_in_fact(9))