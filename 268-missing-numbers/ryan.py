# Runtime: O(1), 3ms (60.77%); Memory: O(1), 18.65MB (71.74%)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result += i - nums[i]

        return result
