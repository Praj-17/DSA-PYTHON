
# Naive
# O(n)
def check_for_prime(n):
    if n<=0: return False
    if n == 1 or n == 2: return True
    if n%2 == 0: return False

    for i in range(2, n//2):
        if n%i == 0:
            return False
    return True

print(check_for_prime(101))

## Optimized

def check_for_prime_standard(n):
    if n<=0: return False
    if n == 1 or n == 2: return True
    if n%2 == 0: return False
    i = 1
    while (i*i <=n):
        if n%i == 0:
            return False
        i+=1
    return True 


#check prime super optimized

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True