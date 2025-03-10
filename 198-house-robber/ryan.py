# Runtime: 0ms (100.00%), Memory: 12.47MB (55.34%)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev1, prev2 = 0, 0

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        
        return prev1
        
