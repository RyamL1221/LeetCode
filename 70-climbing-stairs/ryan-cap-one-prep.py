# Runtime: O(n), 0ms (100.00%); Memory: O(1), 17.67MB (78.09%)
class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
