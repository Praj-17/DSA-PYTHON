# A few direct functions

def left_rotate_slice(l):
    return l[1:] + l[0:1]
def using_pop_append(l):
    l.append(l.pop(0))
    return l
def left_rotate(l1):
    """
    l1 = [1,2,3]
          i   j
    op = [2,3,1]
    """
    if not l1:
        return l1
    first_element = l1[0]
    i = 1
    while i < len(l1):
        # Left shift
        l1[i-1] = l1[i]
        i +=1
    # Now i is 3
    l1[i-1] = first_element
    return l1

print(left_rotate_slice([1,2,3,4,5,6,7,8,9]))

# Left rotate with Steps

"""
l1 = [1,2,3,4,5]
D = 2, N = 5
1   2   3   4   5
i       D

3   2   1   4   5
    i       D

3   4   1   2   5
        i       D

3   4   5   2   1
            i   D
3   4   5   1   2

# D =3 , L = 1,2,3,4,5, 6 N = 6

1   2   3   4   5   6
i           D
4   2   3   1   5   6
    i           D
4   5   3   1   2   6
        i           D
4   5   6   1   2   3

1,2,3,4,5,6 D = 2
1   2   3   4   5   6
I       D
3   2   1   4   5   6
    i       D  
3   4   1   2   5   6
        i       D
3   4   5   2   1   6
            i       D
3   4   5   6   1   2

# 1,2,3,4,5 
""" 

def left_rotate_with_steps(L, D, N):
    i = 0
    while i < D:
        L[i], L[D] = L[D], L[i]
        print(i, D, L)
        D +=1
        i +=1
    # i = 
    return L


def rotateArr(A,D,N):
    #First reversing d elements from starting index.
    # if in any case D is greater than N
    D%=N
    A[0:D]=reversed(A[0:D])
    
    #Then reversing the last n-d elements.
    A[D:N]=reversed(A[D:N])
    
    #Finally, reversing the whole array.
    A[0:N]=reversed(A[0:N])
    return A
print(rotateArr([1,2,3,4,5], D =2, N= 5)) 
