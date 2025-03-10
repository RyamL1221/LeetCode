# Runtime: 104ms (12.67%), Memory: 21.08MB (94.31%)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = global_max = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)
        return global_max
