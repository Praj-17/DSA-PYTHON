def BinarySearch(arr, e):
    if not arr:
        return arr
    high = len(arr)-1
    low = 0

    while low<=high:
        mid = (high + low)//2
        if arr[mid] == e:
            return mid
        elif arr[mid]<e:
            low = mid +1
        else:
            high = mid -1
    return -1


print(BinarySearch([1,2,3,4,5], 4))
        