# Runtime: 0ms (100%); Memory: 13.20MB (60.71%)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_dict:
                result.append(i)
                result.append(nums_dict[diff])
                return result # How can I return an array in one line?
            else:
                nums_dict[nums[i]] = i
        return [] 
