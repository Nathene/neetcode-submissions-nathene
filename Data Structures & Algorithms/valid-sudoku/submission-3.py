class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        row_set = defaultdict(set)
        col_set = defaultdict(set)
        sq_set = defaultdict(set)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    value = board[r][c]
                    if value in row_set[r] or value in col_set[c] or value in sq_set[(r//3, c//3)]:
                        return False
                    row_set[r].add(value)
                    col_set[c].add(value)
                    sq_set[(r//3,c//3)].add(value)
        
        return True