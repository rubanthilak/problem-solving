def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], index]
        else:
            hashmap[num] = index


print(twoSum([2, 7, 11, 15], 9))