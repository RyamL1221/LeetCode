# Runtime: 54ms (26.51%), Memory: 12.37MB (94.36%)
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        def get_coordinates(s):
            quotient, remainder = divmod(s - 1, len(board))
            row = n - 1 - quotient
            col = remainder if quotient % 2 == 0 else n - 1 - remainder
            return row, col
        
        visited = set([1])
        queue = deque([(1, 0)])

        while queue:
            square, moves = queue.popleft()
            if square == n * n:
                return moves

            for i in range(1, 7):
                next_square = square + i
                if next_square > n * n:
                    break
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1

        
