# Runtime: O(n), 67ms (72.14%); Memory: O(n), 18.38MB (34.50%)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        t_count = {}
        freq = {}

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        have, need = 0, len(t_count)
        left = 0
        window_left, window_right = 0, 0
        minimum_window = float("inf")
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            if s[right] in t_count and freq[s[right]] == t_count[s[right]]:
                have += 1
            
            while have == need:
                if minimum_window > (right - left + 1):
                    minimum_window = right - left + 1
                    window_left, window_right = left, right
                freq[s[left]] -= 1
                if s[left] in t_count and freq[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        return s[window_left: window_right + 1] if minimum_window != float("inf") else ""
