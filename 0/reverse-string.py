def reverseString(str: str) -> str:
    result = ''
    for x in range(len(str) - 1, -1, -1):
        result += str[x]
    return result
    
print(reverseString("ruban"))