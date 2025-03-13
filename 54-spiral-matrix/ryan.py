# Runtime: 0ms (100.0%), Memory: 12.48MB (53.01%)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        area = len(matrix) * len(matrix[0])
        spiral = []
        direction = (0, 0)
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while len(spiral) < area:
            for j in range(left, right + 1):
                spiral.append(matrix[top][j])
            top += 1  
            
            for i in range(top, bottom + 1):
                spiral.append(matrix[i][right])
            right -= 1 
            
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][j])
                bottom -= 1  
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    spiral.append(matrix[i][left])
                left += 1 
        return spiral            
