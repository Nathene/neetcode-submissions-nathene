class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [[0, 0, 0]] # max_ele, row, col
        time = 0
        visit = set()
        while heap:
            max_ele, r, c = heapq.heappop(heap)
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit:
                continue
            max_ele = max(max_ele, grid[r][c])
            if r == rows - 1 and c == cols - 1:
                return max_ele
            visit.add((r, c))
            # choose to go right
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if (nr, nc) not in visit:
                    heapq.heappush(heap, [max_ele, nr, nc])

        return -1 
        


