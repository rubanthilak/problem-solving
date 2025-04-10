def factorial(num: int) -> int:
    sum = num
    for i in range(1, num - 1):
        sum *= num - i  
    return sum;

def recursiveFactorial(num: int) -> int:
    if(num == 2):
        return num
    return num * recursiveFactorial(num - 1)

print(recursiveFactorial(5))