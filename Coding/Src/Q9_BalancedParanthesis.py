def balanced_paranthesis(str):
    str = str.replace(" ", "")
    stack = []
    for ch in str:
        if ch == "{":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return "Not Balanced"
            stack.pop()
    if len(stack) != 0:
        return "Not Balanced"
    else:
        return "Balanced"

def balanced_paranthesis_without_stack(str):
    str = str.replace(" ", "")
    counter = 0
    for ch in str:
        if ch == "{":
            counter += 1
        else:
            counter -= 1

    if counter == 0:
        return "Balanced"
    else:
        return "Not Balanced"

str1 = "{{}}"
str2 = " {} } }"
str3 = ""
str4 = " { { { "
print balanced_paranthesis(str1)
print balanced_paranthesis(str2)
print balanced_paranthesis(str3)
print balanced_paranthesis(str4)

print balanced_paranthesis_without_stack(str1)
print balanced_paranthesis_without_stack(str2)
print balanced_paranthesis_without_stack(str3)
print balanced_paranthesis_without_stack(str4)




