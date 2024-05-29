#Faster since it does not require to make any comparisions
def fact(n):
    f = 1
    for i in range(2,n+1):
        f = f*i
    return f
from datetime import datetime

# Get the current time

#Gives recursion depth error for very large inputs
def fact_r(n):
    if n==0 or n ==1:
        return 1
    else:
        return n*fact_r(n-1)
    
# While loop makes comparisons on each iteration hence, it is smaller
def effecient(n):
    if n<0:
        return 0
    elif n ==0 or n ==1:
        return 1
    else:
        fact = 1
        while n>1:
            fact =fact*n
            n -=1
    return fact
now = datetime.now()
print(now)
fact(100000134648914619)
now = datetime.now()
print(now)
effecient(100000134648914619)
now = datetime.now()
print(now)