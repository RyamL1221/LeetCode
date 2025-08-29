# Runtime: O(n), 51ms (59.62%); Memory: O(n), 33.22MB (80.63%)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                result = max(length, result)
        
        return result
