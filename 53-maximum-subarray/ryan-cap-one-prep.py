# Runtime: O(n), 51ms (75.30%); Memory: O(1), 32.85MB (21.94%)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float("-inf")

        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
