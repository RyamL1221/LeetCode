# Runtime: 2ms (12.91%), Memory: 12.40MB (95.46%), Time: O(1), Space: O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[len(words) - 1])
