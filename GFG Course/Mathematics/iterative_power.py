def iterative_power(x,n):
    res = 1
    while n>0:
        if n%2 !=0:
            res =res*x
        x=x*x
        n = n//2
    return res

# Faster! since bitwise operations are used
def iterative_power_binary_operator(x,n):
    res = 1
    while n>0:
        if n&1:
            res =res*x
        x=x*x
        n = n >>1 # Right shift to shift bits right words
    return res

print(iterative_power_binary_operator(4,5))
