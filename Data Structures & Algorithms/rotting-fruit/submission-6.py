"""
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, 
then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits 
remaining. If this state is impossible within the grid, return -1.
"""

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh_fruit = 0
        q = deque()

        rows, cols = len(grid), len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                if grid[r][c] == 2:
                    q.append((r, c, 0)) # [row, col, minutes]

        while q:
            row, col, dist = q.popleft()
            res = max(res, dist)
            for nr, nc in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append([nr, nc, dist + 1])
                    fresh_fruit -= 1

        if fresh_fruit > 0:
            return -1
        return res 
                


