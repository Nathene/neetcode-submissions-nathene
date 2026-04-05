class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]


        rows, cols = len(heights), len(heights[0])
        efforts = [[float("inf")] * cols for _ in range(rows)]
        efforts[0][0] = 0
        visit = set()

        def traverse(heap: list[int]) -> list[int]:
            path = []
            while heap:
                effort, r, c = heapq.heappop(heap)
                visit.add((r, c))
                path.append(effort)

                if r == rows - 1 and c == cols - 1:
                    return effort
                
                for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                        new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                        if new_effort < efforts[nr][nc]:
                            efforts[nr][nc] = new_effort
                            heapq.heappush(heap, [new_effort, nr, nc])
        
        return traverse(heap)

