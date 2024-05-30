def check_prime(n):
    if n<=1:return False
    if n<=3: return True
    if n %2 ==0 or n%3 ==0: return False
    i = 5
    while i*i<=n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i +=6
    return True
def exactly_3_divisors(n):

    count = 0
    for i in range(4, n+1):
        print(i)
        if  n%2 !=0 and check_prime(i) == False:
            print(i)
            divisors = []
            j = 2
            while j*j<=i:
                if i%j ==0:
                    divisors.append(j)
                i +=1
            if len(divisors) ==2:
                count +=1
    return count

def exactly_3_divisors_clever(n):
    """
    1 - 1
    2 - 1,2
    3 - 1,3
    4 - 1,2,4 -- Yes
    5 - 1,5
    6 - 1,2,3,6
    7 - 1,7
    8 - 1, 2,4,8
    9 - 1,3,9  -- Yes
    10 - 1,2,5,10
    16 - 1,2,4,8, 16
    25 - 1,5,25  -- Yes
    There is a simple observation that the number that are yes are  perfect square and their square root is prime.

    """
print(exactly_3_divisors(6))

        
