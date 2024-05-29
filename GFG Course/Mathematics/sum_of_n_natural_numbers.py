# O(1) sulution space is also constant
def sum_4(n):
    return (n*(n+1))//2

#O(n)  iterating once and requires one integer space more
def sum_2(n):
    sum = 0
    for i in range(n+1):
        sum +=i
    return sum

#O(n) but requires to have a whole list in RAM
def sum_3(n): 
    return sum([int(i) for i in range(n+1)])
        
print(sum_4(5))
print(sum_2(4))
print(sum_3(4))