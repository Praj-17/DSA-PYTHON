def chomu(l1):
    return list(set(l1))

## THis is o(n^2)
def with_hash_map(l1):
    map = {}
    for i in l1:
        if i in map.keys():
            pass
        else:
            map[i] = 0
    return map.keys()

def set_theory(l1):
    output = {i for i in l1}
    return output
"""
What if it is sorted?

Example : l1 =[1,1,1,1,2]
i = 1, res = 1 = [1,1,1,1,2]
i = 2, res = 1 = [1,1,1,1,2]
i = 3, rest = 1 = [1,1,1,1,2]
"""

def remove_from_sorted(l1, n):
    res = 1
    for i in range(1, n):
        if l1[res-1] != l1[i]:
            l1[res] = l1[i]
            res+=1



print(with_hash_map([1,2,3,4,1,2,3,4,1,2,3,4,]))