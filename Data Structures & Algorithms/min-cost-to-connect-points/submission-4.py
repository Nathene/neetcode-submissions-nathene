class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        heap = [(0, (points[0][0], points[0][1]))]
        added = set()

        res = 0
        while heap:
            dist, x_y = heapq.heappop(heap)
            if x_y in added:
                continue

            curr_x, curr_y = x_y
            res += dist
            added.add(x_y)

            if len(added) == len(points):
                return res

            for nei_x, nei_y in points:
                if (nei_x, nei_y) in added: continue
                new_dist = abs(curr_x - nei_x) + abs(curr_y - nei_y)
                heapq.heappush(heap, (abs(new_dist), (nei_x, nei_y)))


        return res