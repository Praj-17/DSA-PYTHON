def max_f(a, b):
    if a>b:
        return a
    else:return b
def get_largest(l):
    if not l: return l
    max = l[0]
    for i in l:
        max = max_f(i, max)
    return max
def second_largest(l):
    # The idea is to find the largest element , pop it from the list and then again find the largest
    m = get_largest(l)
    l.pop(l.index(m))
    return get_largest(l)
    
    # the largest elemt

# Praj
def second_largest_single_traversal_if_sorted(l):
    f = 0
    s  = 0
    for i in l:
        if i>=f and i!=f:
            s = f
            f = i
    return None if  s==f else s

def second_largest_single_traversal(l):
    if len(l)<=1:
        return None
    lar = l[0]
    second_largest = None
    for i in l:
        if i>lar:
            second_largest  = lar
            lar = i
        elif i == lar:
            pass
        else:
            if second_largest == None or i>second_largest:
                second_largest = i
    return second_largest
        
print(second_largest_single_traversal([13,72,1,8,24,7,2,7]))
