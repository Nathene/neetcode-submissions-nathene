class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            total = 1

            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                total += dfs(nr, nc)
            
            return total
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res
