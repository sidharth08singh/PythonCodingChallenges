def reverseStringRecursively(str):
    if str is "":
        return str
    else:
        return str[-1] + reverseStringRecursively(str[:-1])  #str[:-1] is the entire string barring last character.


#str = "a"
#print reverseStringRecursively(str)


def reverseListRecursively(list):
    if len(list) is 0:
        return list
    else:
        return [list[-1]] + reverseListRecursively(list[:-1])

list = []
list.append("a")
list.append("b")
list.append("c")
print reverseListRecursively(list)
