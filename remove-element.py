def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == val:
                while nums[j] == val:
                    j -= 1
                nums[i] = nums[j]
                j -= 1
            else:
                count += 1
            i += 1
        return nums

print(removeElement([3,2,2,3], 3))