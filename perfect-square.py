def isPerfectSquare(num: int) -> bool:
    for x in range(1, num // 2 + 1):
        if num // x == x:
            return True
    return False

print(isPerfectSquare(35))