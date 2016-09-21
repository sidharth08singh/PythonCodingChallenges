#Approach 1: Iterate from the last index to first index and store each character in a new string
#Approach 2: Push to stack and pop.
class algorithm:
    def Reverse(self, str):
        rev = "";
        for i in range(len(str)):
            rev = rev + str[len(str) - i - 1]
        return rev

    def ReverseUsingStack(self, str):
        rev = ""
        stack = ()
        for ch in str:
            stack.append(ch)
        while len(stack) != 0:
            rev = rev + stack.pop()
        return rev


obj = algorithm()
str = "a123erf"
print obj.ReverseUsingStack(str)

