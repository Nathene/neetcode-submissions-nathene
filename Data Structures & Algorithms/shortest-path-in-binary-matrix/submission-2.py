class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        def get_neighbors(r: int, c: int) -> list[list[int]]:
            options = [[r + 1, c], [r - 1, c], [r + 1, c + 1], [r - 1, c - 1], [r, c + 1], [r, c - 1], [r - 1, c + 1], [r - 1, c + 1]]
            res = []
            for r, c in options:
                if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] == 1:
                    continue
                res.append([r, c])
            return res

        q = deque([(0, 0, 1)])
        seen = set()
        while q:
            row, col, count = q.popleft()
            if (row, col) in seen:
                continue
            if row == rows - 1 and col == cols - 1:
                return count
            seen.add((row, col))
            for nr, nc in get_neighbors(row, col):
                if (nr, nc) not in seen:
                    q.append([nr, nc, count + 1])
        return -1 
            
        
