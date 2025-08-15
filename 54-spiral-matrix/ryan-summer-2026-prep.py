# Runtime: O(m * n), 0ms, (100.00%); Memory: O(1), 17.96MB (18.47%)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left = top = 0
        bottom = m
        right = n
        result = []

        while left < right and top < bottom:

            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
        
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
        return result
