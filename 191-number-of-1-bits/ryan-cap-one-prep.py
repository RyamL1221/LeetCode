# Runtime: O(log n), 0ms (100.00%); Memory: 17.79MB (51.58%)
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n = n >> 1
        return result
