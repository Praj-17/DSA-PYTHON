def check_sorted_list(l):
    if len(l) ==1 or not l:
        return True
    for i in range(len(l)-1):
        if l[i] >l[i+1]:
            return False
    return True

def easy_sort(l):
    l1 = sorted(l)
    if l == l1:return True
    else: return False

print(check_sorted_list([9,8,7,6,5,4,3,]))
