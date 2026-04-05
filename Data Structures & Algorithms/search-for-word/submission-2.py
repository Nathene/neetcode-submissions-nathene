class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def dfs(r: int, c: int, s: str) -> bool:
            if s == "":
                return True
            if r == rows or c == cols or r < 0 or c < 0 or board[r][c] != s[0] or (r, c) in seen:
                return False
            seen.add((r, c))
            res = dfs(r + 1,  c, s[1:]) or dfs(r - 1,  c, s[1:]) or dfs(r,  c + 1, s[1:]) or dfs(r,  c - 1, s[1:])
            seen.remove((r, c))
            return res
                
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, word): return True
        
        return False


