def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = (len(nums1) + len(nums2))
        itr = ((total_len // 2) - 1) if total_len % 2 == 0 else total_len // 2
        for x in range(0, itr):
            if(len(nums1) == 0):
                nums2.pop(0)
            elif(len(nums2) == 0):
                nums1.pop(0)
            elif(nums1[0] < nums2[0]):
                nums1.pop(0)
            else:
                nums2.pop(0)

        if(total_len % 2 == 0):
            if(len(nums1) == 0):
                return (float(nums2[0]) + float(nums2[1])) / 2
            elif(len(nums2) == 0):
                return (float(nums1[0]) + float(nums1[1])) / 2
            elif(nums1[1] < nums2[0]):
                return (float(nums1[0]) + float(nums1[1])) / 2
            elif(nums2[1] < nums1[0]):
                return (float(nums2[0]) + float(nums2[1])) / 2
            else:
                return (float(nums1[0]) + float(nums2[0])) / 2
        else:
            if(len(nums1) == 0):
                return float(nums2[0])
            elif(len(nums2) == 0):
                return float(nums1[0])
            elif(nums1[0] < nums2[0]):
                return float(nums1[0])
            else:
                return float(nums2[0])
            

print(findMedianSortedArrays([2, 3], [1, 4]))
print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 3], [2, 4, 5]))
print(findMedianSortedArrays([], [1]))
print(findMedianSortedArrays([2,2,4,4], [2,2,2,4,4]))
print(findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17]))