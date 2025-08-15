# Runtime: O(m * n), 0ms (100.00%); Memory: 18.53MB (37.45%)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    if row not in rows:
                        rows.add(row)
                    if col not in cols:
                        cols.add(col)
        
        for row in rows:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        
