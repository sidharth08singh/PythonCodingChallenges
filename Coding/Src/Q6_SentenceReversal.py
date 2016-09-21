def stripp(str):
    i = 0
    while str[i] == " ":
        i = i + 1
    j = len(str) - 1
    while str[j] == " ":
        j = j - 1
    print  "{%d},{%d}", i, j, len(str), str[i], str[j]
    return substring(str,i,j+1)

#str = " Abcdefgh    "
#print str
#print stripp(str)

def substring(str,start, end):
    sstring = ""
    for i in range(start, end):
        sstring = sstring + str[i]
    return sstring

#str = " ##   abcdefgh  #  "
#print substring(str,1,15)

def reverselistUsingStack(list):
    stack = []
    reversedlist = []
    for item in list:
        stack.append(item)
    temp = ""
    counter = len(stack) - 1
    while counter >= 0:
        temp = stack[counter]
        counter = counter - 1
        reversedlist.append(temp)
    return reversedlist

#list = ["A", "B", "C", "D"]
#print reverselistUsingStack(list)

#def reverselistsWithoutStack(list):

sentence = " a abab anan anana   "
sentence = stripp(sentence) #O(n)
dict = {}
words = sentence.split() #O(n)
for word in words:       #O(n)
     if dict.__contains__(word): #Constant
         dict[word] = dict[word] + 1 #Constant
     else:
         dict[word] = 1 #Constant
#words.reverse() #List Reversal
words = reverselistUsingStack(words)
for word in words: #O(n)
     print word + " "


# #Total Time: 4*O(n) + c




