# Runtime: O(n), 96ms (73.24%); Memory: 28.48MB (67.65%)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        left, right = 0, len(height) - 1
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area
