# Runtime 15ms (52.99%), Memory: 20.14MB (35.78%)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        min_len = float("inf")
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if min_len == float("inf") else min_len
            
