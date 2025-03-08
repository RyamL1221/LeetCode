# Runtime: 0ms (100.00%), Memory: 12.54MB (13.79%)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = 0
        nums2_index = 0
        result = []
        while nums1_index < m and nums2_index < n:
            if nums1[nums1_index] < nums2[nums2_index]:
                result.append(nums1[nums1_index])
                nums1_index += 1
            else:
                result.append(nums2[nums2_index])
                nums2_index += 1
        
        while nums1_index < m:
            result.append(nums1[nums1_index])
            nums1_index += 1
        
        while nums2_index < n:
            result.append(nums2[nums2_index])
            nums2_index += 1
        
        for i in range(len(result)):
            nums1[i] = result[i]
