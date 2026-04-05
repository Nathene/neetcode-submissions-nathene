class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows, cols = n, n

        grid = [['.' for _ in range(n)] for _ in range(n)]

        res = []

        cols = set()
        neg_diag = set()
        pos_diag = set()

        def backtrack(r: int) -> bool:
            if r == n:
                curr_solution = ["".join(row) for row in grid]
                res.append(curr_solution)
                return True
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                grid[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                backtrack(r + 1)
                grid[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
            
            return False
        
        backtrack(0)
        return res 

    
        # add in the queen

        # backtrack further

        # remove queen from board, try a different position
