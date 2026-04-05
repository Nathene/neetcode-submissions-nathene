class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        grid[0][0] = 1

        while q:
            r, c, dist = q.popleft()

            if r == n - 1 and c == n - 1:
                return dist
            
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc, dist + 1))

        return -1        
