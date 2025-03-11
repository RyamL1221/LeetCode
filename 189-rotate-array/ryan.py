# Runtime: 4ms (56.06%), Memory: 24.09MB (21.47%)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        first_half = nums[len(nums) - k:]
        second_half = nums[:len(nums) - k]
        i = 0
        for index in range(len(first_half)):
            nums[i] = first_half[index]
            i += 1
        for index in range(len(second_half)):
            nums[i] = second_half[index]
            i += 1
