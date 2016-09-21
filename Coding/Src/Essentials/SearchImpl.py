#returns index of the element if found, else returns -1.
class SearchImpl:
    def BinSearch(self, arr, searchItem):
        low,high = 0, len(arr)-1
        arr = sorted(arr)
        print arr
        while(low <= high):
            mid = (low + high)/2
            if(arr[mid] == searchItem):
                return mid
            elif(arr[mid] > searchItem):
                high = mid-1
            else:
                low = mid+1
        return -1

obj = SearchImpl()
arr = (11,2,19,12,22,45,33,23)
print obj.BinSearch(arr,12)