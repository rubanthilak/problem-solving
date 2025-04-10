from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    hsh = {}
    for n in nums:
        if hsh.get(n) == 1:
            return True
        else: 
            hsh[n] = 1
    return False

print(hasDuplicate([1,2,3,4,5]))