# naive

def check_prime(n):
    if n<=1:return False
    if n<=3: return True
    if n%2 ==0 or n%3==0: return False
    i = 5
    while(i*i<=n):
        if n%i == 0 or n%(i+2) == 0:
            return False
        i +=6
    return True



def prime_factors(n):
    factors = []
    for i in range(2, n+1):

        if n%i ==0:

            #now check if it is prime
            if check_prime(i):
                print(i)
                x = i
                while n%x == 0:
                    factors.append(i)
                    x = x*i
    return factors

print(prime_factors(100))

