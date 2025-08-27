# Runtime: O (n log n), 62ms (12.58%); Memory: O(n), 18.51MB (58.94%)
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            curr = 0
            while i > 0:
                if i % 2 == 1:
                    curr += 1
                i = i >> 1
            result.append(curr)
        return result
