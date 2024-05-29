def get_gcf(n, m):
    
    if m == 0:
        return n 
    if n == 0:
        return m
    if m == 1 or n == 1:
        return 1
    if n == m:
        return n
    elif m>n:
        greater = m
        smaller = n
    else:
        greater = n
        smaller = m
    if greater%smaller == 0:
        return smaller
    else:
        for i in range(smaller, 1, -1):
            if greater%i == 0 and smaller%i ==0:
                return i
        else: return 1


# This is wuclidean algorithm

def gcf_euclidien(a, b):
    if a == 0:
        return b 
    if b == 0:
        return a
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b -a
    return a



# optimized Euclidean 

"""
The time complexity for this will be 

O(log(min(a,b)))

"""
def optimized_euclidean(a, b):
    if b ==0:
        return a
    return optimized_euclidean(b, a%b)

print(optimized_euclidean(12,15))
        