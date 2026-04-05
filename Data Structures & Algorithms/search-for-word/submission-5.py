class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()
    
        def backtrack(r: int, c: int, idx: int) -> bool:
            if idx == len(word): return True
            if r == rows or c == cols or r < 0 or c < 0 or \
                (r, c) in seen or board[r][c] != word[idx]:
                return False
            
            seen.add((r, c))
            
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if backtrack(nr, nc, idx + 1): return True
            
            seen.remove((r, c))
            return False
            

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0): return True
        
        return False
