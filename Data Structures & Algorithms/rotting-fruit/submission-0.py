from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        
        time = 0
        while q:
            r, c, mins = q.popleft()
            time = max(time, mins)
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c-1]]:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                q.append((nr, nc, mins + 1))
       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        
        return time

        # 2, 2 - t = 0
        # 1, 2, 2, 1 - t = 2
        # 1, 1 - t = 3

