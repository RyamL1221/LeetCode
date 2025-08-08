# Runtime: O(n), 14ms (84.22%); Memory: O(n), 17.96MB (33.70%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right = 0, 1
        letters = set()
        letters.add(s[left])
        max_length = 1
        while right < len(s):
            if s[right] not in letters:
                letters.add(s[right])
            else:
                current_length = right - left
                max_length = max(max_length, current_length)
                while s[left] != s[right]:
                    letters.remove(s[left])
                    left += 1
                left += 1
            right += 1
        current_length = right - left
        max_length = max(current_length, max_length)
        return max_length
