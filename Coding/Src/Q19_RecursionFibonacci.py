def fibR(n):
    series = []
    if n is 0:
        return [0]
    if n is 1:
        default = [0,1]
        return default
    else:
        series = series + fibR(n-1)
        if n is not 1:
            nextterm = series[n-2] + series[n-1]
            series.append(nextterm)
        return series

list = []
n=2
list = fibR(n-1)
print list

def fibNthTerm(n):
    if n is 0:
        last = 0
        secondlast = 0
        return secondlast,last
    elif n is 1:
        last = 1
        secondlast = 0
        return secondlast,last
    else:
        secondlast,last = fibNthTerm(n-1)
        temp = last
        last = last + secondlast
        secondlast = temp
        return secondlast, last


n=2
a,b = fibNthTerm(n-1)
print b