# Runtime: O(n), 0ms (100.00%); Memory: 17.64MB (86.36%)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_helper(nums):
            rob1, rob2 = 0, 0
            for i in range(len(nums)):
                temp = max(rob2, rob1 + nums[i])
                rob1 = rob2
                rob2 = temp
            return rob2
        
        n = len(nums)
        return max(rob_helper(nums[1:]), rob_helper(nums[0:n - 1]))
