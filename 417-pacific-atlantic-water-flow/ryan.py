# Runtime: 57ms (18.64%); Memory: 19.45MB (46.28%)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        atl, pac = set(), set()
        
        def dfs(row, col, visited, prev_height):
            if (row, col) in visited or not row in range(m) or not col in range(n) or heights[row][col] < prev_height:
                return
            visited.add((row, col))

            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
        
        for row in range(m):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, n - 1, atl, heights[row][n - 1])

        for col in range(n):
            dfs(0, col, pac, heights[0][col])
            dfs(m - 1, col, atl, heights[m - 1][col])

        result = []
        for row in range(m):
            for col in range(n):
                if (row, col) in pac and (row, col) in atl:
                    result.append([row, col])
        
        return result
