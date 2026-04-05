class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r: int, c: int, visit: set, prev: int) -> None:
            if (r, c) in visit or not (0 <= r < rows) or not (0 <= c < cols) or \
                heights[r][c] < prev:
                return
            
            visit.add((r, c))
            for nr, nc in [[r + 1, c], [r - 1,c], [r, c + 1], [r, c - 1]]:
                dfs(nr, nc, visit, heights[r][c])
        
        pac, atl = set(), set()

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res

        
    

