def unique(s):
    s = s.lower().replace(" ","")
    dict = {}
    for ch in s:
        if dict.__contains__(ch):
            return "False"
        else:
            dict[ch] = 1
    return "True"

str = "aaa"
str1 = "abc"
str3 = "A a b c D"
print unique(str)
print unique(str1)
print unique(str3)
