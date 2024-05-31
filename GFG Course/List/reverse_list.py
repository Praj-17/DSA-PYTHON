def reverse_list(l):
    return l[::-1]

def reversed_list_2(l):
    return list(reversed(l))
def reversed_list_2(l):
    l.reverse()
    return l
def reversed_list_3(l):
    ans = []
    for i in range(len(l)+1, 0, -1):
        ans.append(i)
    return ans

def reverse_using_swapping(l):
    if len(l) <=1:
        return l
    i = 0
    j = len(l)-1
    while i<=j:
        l[i], l[j] =l[j] , l[i]
        i +=1
        j -=1
    return l
print(reverse_using_swapping([1,2,3,4,5,6,]))