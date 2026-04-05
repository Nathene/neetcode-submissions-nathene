class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        # We pass masks as arguments to keep them local to each recursive branch
        def backtrack(r: int, cols: int, pos_diag: int, neg_diag: int) -> None:
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                # Using (r - c + n) to keep the index positive for bit shifting
                if (cols & (1 << c)) or \
                   (pos_diag & (1 << (r + c))) or \
                   (neg_diag & (1 << (r - c + n))):
                    continue
                
                # Choose
                board[r][c] = "Q"
                
                # Explore (passing updated masks to the next level)
                # Note: No need to manually 'undo' the masks because 
                # they are passed by value in the function call!
                backtrack(
                    r + 1, 
                    cols | (1 << c), 
                    pos_diag | (1 << (r + c)), 
                    neg_diag | (1 << (r - c + n))
                )
                
                # Backtrack (Un-choose)
                board[r][c] = "."

        backtrack(0, 0, 0, 0)
        return res