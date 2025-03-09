# Runtime 0ms (100.00%), Memory: 12.45MB (52.01%)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for i in range(len(digits)):
            num += str(digits[i])
        num = int(num)
        num += 1
        result = []
        while num > 0:
            result.insert(0, num % 10)
            num //= 10
        return result
        
