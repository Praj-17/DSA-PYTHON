def smaller_elements(l, n):
    ans = []
    for i in l:
        if i<n:
            ans.append(i)
    return ans
def smaller_elemets_comprehension(l, n):
    return [i for i in l if i<n]

print(smaller_elemets_comprehension([1,2,3,4,5,6,7,8,9,], 5))