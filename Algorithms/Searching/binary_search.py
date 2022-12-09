
def binary_search_iterative(arr:list, key):
    high = len(arr)-1
    low = 0
    while  high - low > 1:
        mid = (high-low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid
            
    if arr[low] == key:
        print("Found At Index", low)
    elif arr[high] == key:
        print("Found At Index", high)
    else:
        print("Not Found")
def binary_search_recusrsive(arr, high, low, key):
    
    if low > high:
        return 
    mid = (high +low)//2

    if arr[mid] == key:
        return mid
    elif arr[mid]<key:
        return binary_search_recusrsive(arr, high,mid + 1, key)
    else:
        return binary_search_recusrsive(arr, mid, low, key)

print(binary_search_iterative([1,2,3,4,5,6,7,8,9], 5))
print(binary_search_recusrsive([1,2,3,4,5,6,7,8,9],9,0, 5))