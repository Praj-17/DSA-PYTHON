def mergesort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]
  
  left = mergesort(left)
  right = mergesort(right)
  return merge(left, right)

def merge(left, right):
  result = []
  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  if len(left) > 0:
    result.extend(left)
  if len(right) > 0:
    result.extend(right)
  return result
