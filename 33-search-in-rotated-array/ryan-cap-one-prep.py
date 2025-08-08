# Runtime: O(log n), 0ms (100.00%); Memory: 18.00MB (90.94%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else: 
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return result
