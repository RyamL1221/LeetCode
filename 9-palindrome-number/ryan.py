# Runtime: 4ms (89.71%), Memory: 12.42MB (13.35%)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]
