class algorithm:
    def MissingEl(self, arr1, arr2):
        dict = {}
        for i in arr1:
            if dict.__contains__(i):
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1

        for i in arr2:
            if dict.__contains__(i):
                dict[i] = dict[i] - 1
            else:
                dict[i] = 1

        answer, flag = 0,0
        for i in dict:
            if dict[i] != 0:
                answer = i
                flag = flag+1

        if flag == 1:
            return answer
        else:
            return "invalid"


obj = algorithm()
arr1 = (1,2,2,4, 8,8)
arr2 = (2,1,2,8,4)
print obj.MissingEl(arr1,arr2)