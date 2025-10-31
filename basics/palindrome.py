import string

def palindrome(str: string) -> bool:
    return str == str[::-1]

def indexPalindrome(str:string) -> bool:
    for i in range(0, len(str) // 2):
        if(str[i] != str[len(str) - (i + 1)]):
            return False
    return True

print(indexPalindrome('o'))