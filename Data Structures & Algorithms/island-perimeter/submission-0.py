class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        seen = set()

        def search(r, c):
            if grid[r][c] == 1:
                seen.add((r, c))
            total = 4
            if r < rows - 1  and grid[r+1][c] == 1:
                total -= 1
            if r > 0 and grid[r-1][c] == 1:
                total -= 1
            if c < cols - 1 and grid[r][c+1] == 1:
                total -= 1
            if c > 0 and grid[r][c-1] == 1:
                total -= 1
            
            return total

            
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == 1:
                    res += search(r, c)
        
        return res