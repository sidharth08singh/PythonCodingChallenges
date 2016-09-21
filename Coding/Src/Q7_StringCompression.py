def removeSpaces(s):
    space = [' ']
    snew = ""
    for ch in s:
        if ch not in space:
            snew = snew + ch
    return snew


def StringCompress(s):
    s = removeSpaces(s)
    dict = {}
    compressedstr = ""
    for ch in s:                       #O(n
        if dict.__contains__(ch):
            dict[ch] = dict[ch] + 1
        else:
            dict[ch] = 1
    for ch in dict:
        compressedstr += ch
        temp = str(dict[ch])
        compressedstr += temp
    return compressedstr





#def StringCompress(s):


s = "acbabccbfgvv"
print StringCompress(s)