class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        heap = [[0, 0]]
        visit = set()
        res = 0
        while len(visit) < n:
            cost, i = heapq.heappop(heap)
            if i in visit:
                continue
            visit.add(i)
            res += cost

            for j in range(n):
                if j in visit:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (dist, j))

        return res

            
        

                
