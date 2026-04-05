class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        queue = deque([(0, 0, 0)]) # [row, col, steps]
        rows, cols = len(grid), len(grid[0])
        seen = set((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for _ in range(len(queue)):
                row, col, steps = queue.popleft()
                if row == rows - 1 and col == cols - 1:
                    return steps
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and ((nr, nc)) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
        
        return -1
                




 
