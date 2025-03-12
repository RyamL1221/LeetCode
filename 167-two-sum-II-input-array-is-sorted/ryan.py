# Runtime: 8ms (29.49%), Memory: 12.89MB (69.71%)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return -1
        
