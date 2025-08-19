# Runtime: O(n^2) 127ms (76.33%); Memory: O(1) 17.75MB (65.89%)
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            left, right = i, i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                result += 1
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                result += 1
                left -= 1
                right += 1
            
        return result
