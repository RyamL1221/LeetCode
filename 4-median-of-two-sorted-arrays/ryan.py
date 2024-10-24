# Runtime: 5ms (95.90%), Memory: 11.99 MB (9.89%) 
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        for i in range(len(nums1)):
            merged.append(nums1[i])
        for i in range(len(nums2)):
            merged.append(nums2[i])
        merged.sort()
        if len(merged) % 2 is 0:
            return float((merged[len(merged) // 2 - 1] + merged[len(merged) // 2])) / 2
        else:
            return merged[len(merged) / 2]
        