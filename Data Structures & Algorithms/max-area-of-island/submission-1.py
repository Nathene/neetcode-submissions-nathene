class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r, c))

            opts = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            res = 1
            for row, col in opts:
                res += dfs(row, col)
            return res
        longest = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    curr_island = dfs(r, c)
                    longest = max(longest, curr_island)
        
        return longest