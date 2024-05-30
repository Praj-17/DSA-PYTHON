def power(x, n):
    if x == 0:
        return 0
    if n ==1:
        return x
    if x == 1 or n == 0:
        return 1
    
    return x**n

# Complexisty - Both space and time O(Log(n))
def optimized_power(x, n):
        if x == 0:
            return 0
        if n ==1:
            return x
        if x == 1 or n == 0:
            return 1
        if n%2 ==0:
             return optimized_power(x, n//2)*optimized_power(x,n/2)
        else:
             return optimized_power(x, n-1)*x
    

print(optimized_power(2, 5))