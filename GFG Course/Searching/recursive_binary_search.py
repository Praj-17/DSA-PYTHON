def BinarySearch(arr, n, low, high):
    mid = (low+high)//2
    if low>=high:
        return -1
    if arr[mid] == n:
        return mid
    if arr[mid] <n:
        return BinarySearch(arr, n, mid+1, high)
    if arr[mid] >n:
        return  BinarySearch(arr, n, low,high-1 )
    
def wrapper(arr, n):
    if not arr:
        return arr
    return BinarySearch(arr, n, 0, len(arr)-1)

print(wrapper([1,2,3,4,4,4,4,5,5,6,7,8], 5))