def max_f(a,b):
    if a>b:
        return a
    else:
        return b
def largest_element_in_a_list(l):
    if not l: return None
    max = 0
    for i in l:
        max = max_f(max, i)
    return max
print(largest_element_in_a_list([1,2,3,4,5,6,7,8,9,]))