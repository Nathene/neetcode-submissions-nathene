class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)] # [total_weight, row, col, highest]
        rows, cols = len(grid), len(grid[0])

        visit = set((0, 0))

        while heap:
            highest, row, col = heapq.heappop(heap)
            if row == rows - 1 and col == cols - 1:
                return highest
            for nr, nc in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(heap, (max(highest, grid[nr][nc]), nr, nc))

        

        return -1