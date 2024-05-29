
# Naive solution O(n) time 
def get_all_divisors(n):
    ans = [1]

    i = 2
    while i<=n:
        if n%i==0:
            ans.append(i)
        i +=1
    return ans

# print(get_all_divisors(100))

"""
Note the following 2 things before calculating the divisor of 2 numbers

1. Divisors always occur in Pairs. That is For every divisor there is another divisor with which the produc becomes equal to the number

30: (1,30), (2,15), (3,10), (5,6)

2. Also, One of the divisors is always less than or equal to the square root of the number


"""

# This does not maintain sequence
def optimized_divisors(n):
    ans = [1]
    i = 2
    while i*i<=n:
        if n%i == 0:
            ans.append(i)
            if i != n//i:
                ans.append(n//i)
        i +=1
        
    return ans

# This does not maintain sequence
def optimized_divisors_sequenced(n):
    ans = [1]
    i = 2
    while i*i<n:
        if n%i == 0:
            ans.append(i)
        i +=1
    # i is close to the square root now

    while i>=1:
        if n%i ==0:
            ans.append(n//i)
        i -=1
    return ans

print(optimized_divisors_sequenced(100))