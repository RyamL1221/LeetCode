# Runtime: 31ms (5.25%), Memory: 13.59MB (90.33%)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_counter = []
        for num in nums:
            num_counter.append(num)
        num_counter = Counter(num_counter).most_common()
        return num_counter[0][0]
