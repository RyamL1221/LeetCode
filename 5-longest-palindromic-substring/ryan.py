class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestPal = ""
        for i in range(len(s)):
            oddPalindrome = self.expandAroundCenter(s, i, i)
            if(len(oddPalindrome) > len(longestPal)):
                longestPal = oddPalindrome
            evenPalindrome = self.expandAroundCenter(s, i, i + 1)
            if(len(evenPalindrome) > len(longestPal)):
                longestPal = evenPalindrome
        return longestPal
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]       
            
   
        