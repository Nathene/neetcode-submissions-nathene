class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        def dfs(row: int, col: int) -> int:
            if row == rows - 1 and col == cols - 1:
                return 1
            res = 0
            seen.add((row, col))
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = row + dr, col + dc
                if (nr, nc) not in seen and 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    res += dfs(nr, nc)
            seen.remove((row, col))
            
            return res
        
        return dfs(0, 0)