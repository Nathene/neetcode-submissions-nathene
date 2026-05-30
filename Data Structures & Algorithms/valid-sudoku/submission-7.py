class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical = defaultdict(set)
        horizontal = defaultdict(set)
        squares = defaultdict(set)

        rows, cols = 9, 9
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".": continue
                val = board[r][c]

                sq = (r // 3, c // 3)

                if val in vertical[c] or val in horizontal[r] or val in squares[sq]:
                    return False
                
                vertical[c].add(val)
                horizontal[r].add(val)
                squares[sq].add(val)
        
        return True
