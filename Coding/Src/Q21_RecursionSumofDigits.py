def sumofdigits(n):
    if n is 0:
        return n
    else:
        return (n % 10) + sumofdigits(n/10)

print sumofdigits(1234001)