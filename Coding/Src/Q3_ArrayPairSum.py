#Approach 0: Quadratic Time - Consider all pairs possible using 2 for loops.
#Approach 1: Using Hash Tables.
#Approach 2: Using Dynamic Programming.
class algorithm:
    def ArrayPairSum(self, arr, sum):
        dict = {}
        for i in arr:
            if (dict.__contains__(i)):
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1

        for i in arr:
            dict[i] = dict[i] - 1
            if (dict.__contains__(sum-i) and dict[sum-i] != 0):
                print "YES"
                return
            dict[i] = dict[i] + 1
        print "NO"

    def ArrayPairSumUsingSorting(self, arr, sum):
        arr = sorted(arr)
        print arr
        i, j = 0,len(arr)-1
        while i < j:
            if ((arr[i] + arr[j]) == sum):
                return "TRUE"
            elif ((arr[i] + arr[j]) > sum):
                j = j - 1;
            else:
                i = i + 1;
        return "FALSE"

obj = algorithm()
arr = (1,2,3,5,4,9,8)
print obj.ArrayPairSumUsingSorting(arr,0)