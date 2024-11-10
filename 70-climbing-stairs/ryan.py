# 0ms (100%), 11.56MB (62.10%)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev1 = 1
        prev2 = 1
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1
