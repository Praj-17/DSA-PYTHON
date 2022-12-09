def linear_search(arr, key):
    for i in arr:
        if i == key:
            return arr.index(i)
        else:
            print('not Found')

    