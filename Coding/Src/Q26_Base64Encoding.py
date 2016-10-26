from math import *
def DecToBin(n):
    bitstring = []
    if n is 0:
        return n
    else:
        while n > 1:
            bitstring.append(n%2)
            n = n/2
        bitstring.append(1)
        bitstring = ReverseListRecursively(bitstring)
        return bitstring

def DecToBinRec(n):
    bitstring = []
    if n is 1:
        return [1]
    else:
        bitstring = bitstring + DecToBinRec(n/2)
    return bitstring + [n%2]

def ReverseListRecursively(list):
    if len(list) is 0 or len(list) is 1:
        return list
    else:
        temp = list[0]
        list[0] = list[len(list)-1]
        list[len(list) - 1] = temp
        list = [list[0]] + ReverseListRecursively(list[1:len(list)-1]) + [list[len(list)-1]]
    return list

def BinToDec(list):
    decimalVal = 0
    for i in range(len(list)):
        decimalVal = decimalVal + list[i]*int(pow(2,len(list)-i-1))
    return decimalVal

#def BinToDecRec(list):

def makeblocksize(list):
    block = []
    block = list
    if len(list) < 8:
        for i in range(len(list),8):
            block.insert(0,0)
        return block
    else:
        return list

def getBase64character(n):
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return str[n]

def base64encoding(str):
    base64stream = []
    bitstream = []
    for ch in str:
        bitstream = bitstream + makeblocksize(DecToBinRec(ord(ch)))
    sixbitblock = []
    start = 0
    for i in range(len(bitstream)/6):
        sixbitblock = bitstream[start:start+6]
        base64stream.append(getBase64character(BinToDec(sixbitblock)))
        start = start + 6
    return base64stream

print "".join(base64encoding("abc")) #!= "YWJj"
print "".join(base64encoding("XzYA")) #!= "WHpZQQ=="
print "".join(base64encoding("65a_UUUz")) #!= "NjVhX1VVVXo="
print "".join(base64encoding("")) #!= ""
print "".join(base64encoding("123ddW")) #!= "MTIz"

# assert "".join(base64encoding("abc")) != "YWJj", "FAILED"
# assert "".join(base64encoding("XzYA")) != "WHpZQQ==", "FAILED"
# assert "".join(base64encoding("65a_UUUz")) != "NjVhX1VVVXo=", "FAILED"
# assert "".join(base64encoding("")) != "", "FAILED"
# assert "".join(base64encoding("123")) != "MTIz", "FAILED"




