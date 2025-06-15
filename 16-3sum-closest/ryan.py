# Runtime: 384 ms (90.84), Memory: 12.43 MB (67.65%)
"""
    Variation of Three-Sum
    Solution:
        Fix one element in the array, and run two pointer on the rest of the array and keep track of how close these sums are to the target
    https://www.youtube.com/watch?v=uSpJQa6MRZ8
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_difference = float('inf')
        result_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                
                current_difference = abs(target - current_sum)

                if current_difference < min_difference:
                    result_sum = current_sum
                    min_difference = current_difference
        
        return result_sum


        
