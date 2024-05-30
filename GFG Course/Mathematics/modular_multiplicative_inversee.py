#Given two integers ‘a’ and ‘m’. The task is to find the smallest modular multiplicative inverse of ‘a’ under modulo ‘m’. if it does not exist then return -1

def modularInverse(a, m):
    """
    A number x is said to modular multiplicative inverse of a under m if (a%m * x%m)%m = 1. Since x%m lies in between 0 to m-1 and we need to find the smallest x. Thus we will simply iterate over all possible values of x%m i.e from 0 to m-1 and will check if the condition holds true.
    """

    # taking mod of a with m
    a=a%m
    
    # For every number x, check if (a*x)%m is 1
    for x in range(1,m):
        if((a*x)%m==1):
            return x
    
    return -1
