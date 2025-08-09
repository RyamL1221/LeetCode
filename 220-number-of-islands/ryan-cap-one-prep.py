# Runtime: 317ms (10.34%); Memory: 25.56MB (17.86%)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        m = len(grid)
        n = len(grid[0])
        result = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

            while queue:
                row, col = queue.popleft()
                visited.add((row, col))
                for dr, dc in directions:
                    if row + dr in range(m) and col + dc in range(n) and grid[row + dr][col + dc] == "1" and (row + dr, col + dc) not in visited:
                        queue.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    result += 1
        
        return result
