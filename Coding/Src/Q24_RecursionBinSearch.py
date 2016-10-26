def binsearchrecursively(list1, item):
    low = 0
    high = len(list1)-1
    if low <= high:
        mid = (low + high)/2
        if item is list1[mid]:
            return mid
        elif item < list1[mid]:
            pos = binsearchrecursively(list1[0:mid], item)
        else:
            pos = (mid+1) + binsearchrecursively(list1[mid+1:high+1], item)
    else:
        return "not present"
    return pos

arr = [2, 3, 4, 5, 6, 7, 8]
print binsearchrecursively(arr, 8)
