class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r: int, c: int) -> None:
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    total += 1
                    dfs(r, c)
        
        return total