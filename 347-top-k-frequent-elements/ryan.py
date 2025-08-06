# Runtime: O(n), 23ms (15.29%); Memory: O(n), 20.04MB (5.89)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        frequency_arr = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            num = nums[i]
            frequency[num] = frequency.get(num, 0) + 1
        
        for num, count in frequency.items():
            frequency_arr[count].append(num)
        
        result = []
        for i in range(len(frequency_arr) - 1, 0, -1):
            for j in range(len(frequency_arr[i])):
                result.append(frequency_arr[i][j])
                if len(result) >= k:
                    return result
