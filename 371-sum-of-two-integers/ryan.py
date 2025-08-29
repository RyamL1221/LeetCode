# Runtime: O(1), 0ms (100.00%); Memory: O(1), 17.85MB (29.54%)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b != 0:
            temp = (a & b) << 1
            a = (a ^ b) & mask
            b = temp & mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a
