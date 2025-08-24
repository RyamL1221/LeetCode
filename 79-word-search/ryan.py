# Runtime: 7973ms (5.00%); Memory: 18.00MB (39.80%)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word): return True
            if (row not in range(m) or
                col not in range(n) or
                (row, col) in path or
                board[row][col] != word[i]): return False
            
            path.add((row, col))

            result = (dfs(row + 1, col, i + 1) or
                    dfs(row, col + 1, i + 1) or
                    dfs(row - 1, col, i + 1) or
                    dfs(row, col - 1, i + 1))
            
            path.remove((row, col))
            return result
        
        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0): return True
        
        return False
