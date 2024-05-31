def even_odd(li):
    evens = []
    odds = []
    for i in li:
        if i%2 ==0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds
def even_odd_comprehension(l):
    return [i for i in l if i%2==0], [i for i in l if i%2==1]

print(even_odd_comprehension([1,2,3,8,4,5,66,7,99]))