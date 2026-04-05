class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        atl_set = set()
        def atlantic(r, c, biggest):
            if (r, c) in atl_set or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < biggest:
                return
            atl_set.add((r, c))
            atlantic(r+1, c, heights[r][c])
            atlantic(r-1, c, heights[r][c])
            atlantic(r, c+1, heights[r][c])
            atlantic(r, c-1, heights[r][c])

        pac_set = set()
        def pacific(r, c, biggest):
            if (r, c) in pac_set or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < biggest:
                return
            pac_set.add((r, c))
            pacific(r+1, c, heights[r][c])
            pacific(r-1, c, heights[r][c])
            pacific(r, c+1, heights[r][c])
            pacific(r, c-1, heights[r][c])

        for r in range(rows):
            pacific(r, 0, heights[r][0])
            atlantic(r, cols - 1, heights[r][cols - 1])
        for c in range(cols):
            pacific(0, c, heights[0][c])
            atlantic(rows - 1, c, heights[rows - 1][c])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl_set and (r, c) in pac_set:
                    res.append([r, c])
        
        return res