# Runtime: 0ms (100%), Memory: 11.70MB (10.37%)
class Solution(object):
    def generate(self, numRows):
        res = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res
