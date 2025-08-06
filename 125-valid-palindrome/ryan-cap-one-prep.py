# Runtime: O(n), 5ms (97.87%); Memory: O(n) 13.93MB (37.96%)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', "", s)
        s = s.lower()
        if s != s[::-1]:
            return False
        else: 
            return True
