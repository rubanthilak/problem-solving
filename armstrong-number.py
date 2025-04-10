def isArmstrongNumber(num: int) -> bool:
    sum = 0
    temp = num
    while(temp > 0):
        sum += ((temp % 10)**3)
        temp = temp//10
    return sum == num

print(isArmstrongNumber(371))