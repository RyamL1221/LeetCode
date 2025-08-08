# Runtime: O(log n), 0ms (100.00%); Memory: O(1), 18.26MB (9.23%)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(nums[left], result)
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return result
