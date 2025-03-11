# Runtime: 59ms (14.24%), Memory: 13.32MB (76.38%)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
                n -= 1
            else:
                i += 1
        k = len(nums)
        return k
