# Prime numbers till a given number
# This is naive method O(n*root(n))
def is_prime(n):
    if n<=1:
        return False
    if n == 2 or n ==3:
        return True
    if n%2==0 or n%3 ==0:
        return False
    i = 5
    while (i*i<=n):
        if n%i == 0 or n%(i+2) == 0:
            return False
        i +=6
    return True
def get_all_primes_till(n):
    if n == 1:
        print(1)
    if n == 2:
        print(1,2)

    i = 3
    while (i<=n):
        if is_prime(i):
            print(i)
        i+=2


# Anyways you will have to check for the prime number so the optimization lies in the iterating all numbers from that number.

"""
See the following example

if n == 25
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
remove 1 as it is not prime
2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25

remove all even numbers except for 2
1,3,5,7,9,11,13,15,17,19,21,23,25

remove all numbers divisible by 3 and 5 and even 7 except for them
2,3,5,7,11,13,17,19,23
"""

# Praj solution this is also O(nroot(n))
def optimized_seive(n):
    if n<=1:
        print([])
    if n >=3:
        print(2)
        print(3)
    i = 5
    while (i+2<=n):
        if i%2 == 0 or i%3 ==0:
            continue
        if is_prime(i):
            print(i)
        if is_prime(i+2):
            print(i+2)
        i +=6


# Traditional Seive Solution

"""

Create an array of shape n+1 and Assign True values to all of them!

"""

def sieve_best(n):
    if n<=1:
        return
    isPrime = [True]*(n+1)
    i=2
    while i*i <=n:
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j]=False
        i +=1
    for i in range(2,n+1):
        if isPrime[i]:
            print(i, " ",  end = "")

sieve_best(25000000)

