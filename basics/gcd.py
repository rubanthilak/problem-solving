def calcuateGcd(a,b):
    if b == 0:
        return a
    else:
        return calcuateGcd(b, a % b)


print(calcuateGcd(12,54))