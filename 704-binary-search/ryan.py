# Runtime: O(log n), 0ms (100.00%); Memory: O(1), 18.65MB (73.67%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
