class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2 ** 31 - 1
        water = -1
        chest = 0

        q = deque()
        rows, cols = len(grid), len(grid[0])
        # find treasure
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c, 0])
        

        while q:
            r, c, dist = q.popleft()
            grid[r][c] = min(grid[r][c], dist)

            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == inf:
                    q.append([nr, nc, dist + 1])
        

