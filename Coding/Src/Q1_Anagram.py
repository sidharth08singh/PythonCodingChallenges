#Anagram
#Input : String1, String2
#Output: Boolean
class algorithm:
    def anagram(self, str1, str2):
        #Create an array for each of 26 characters.
        #Initialize each index of the array to 0.
        #Ignore cases by converting all to lower case.
        #Iterate through str1 & increment the array index by 1 corresponding to the character.
        #Iterate through str2 & decrement the array index by 1 corresponding to the character.
        #Iterate through the array. If all indices contain 0, then return true; otherwise return false.

        str1 = str1.lower().replace(" ","")
        str2 = str2.lower().replace(" ","")
        a = [0] * 100
        for c in str1:
            a[ord(c) - 97] = a[ord(c)-97] + 1
        for c in str2:
            a[ord(c) - 97] = a[ord(c)-97] - 1
        for itr in a:
            if(itr != 0):
                return False
        return True

obj = algorithm()
str1 = "abc"
str2 = "a c ba"
print obj.anagram(str1,str2)