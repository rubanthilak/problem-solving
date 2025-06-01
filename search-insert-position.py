def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i<=j:
            mid = (i+j) // 2
            if(nums[mid] == target):
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return i
            
print(searchInsert([1,3], 0))