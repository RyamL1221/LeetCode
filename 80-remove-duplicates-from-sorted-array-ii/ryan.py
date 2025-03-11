# Runtime: 88ms (10.65%), Memory: 15.28MB (57.29%)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 2]:
                del nums[i + 2]
            else:
                i += 1
        return len(nums)
            
        
