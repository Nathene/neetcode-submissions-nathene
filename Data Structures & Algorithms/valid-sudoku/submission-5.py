class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        row_set = [0] * 9
        col_set = [0] * 9
        sq_set = [0] * 9
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    value = int(board[r][c])
                    idx = (r // 3) * 3 + (c // 3)
                    if (row_set[r] >> value) & 1 or (col_set[c] >> value) & 1 or (sq_set[idx] >> value) & 1:
                        return False
                    row_set[r] |= (1 << value)
                    col_set[c] |= (1 << value)
                    sq_set[idx] |= (1 << value)
        
        return True