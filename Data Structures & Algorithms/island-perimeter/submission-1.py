class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(r: int, c: int) -> int:
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0:
                return 1
            
            visit.add((r, c))
            res = 0
            for nr, nc in [[r + 1,c ], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if (nr, nc) not in visit:
                    res += dfs(nr, nc)
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        return 0
        

            
