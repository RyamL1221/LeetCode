# Runtime: 28ms (21.20%); Memory: 26.42MB (5.66%)
# How can we do this using sets?
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            else:
                nums_dict[nums[i]] = True
        return False
