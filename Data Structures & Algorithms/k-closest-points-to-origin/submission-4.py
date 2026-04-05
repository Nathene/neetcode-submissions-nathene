class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = (x ** 2) + (y **2)
            heapq.heappush(heap, [dist, x, y])
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            k -= 1
            res.append([x, y])
        
        return res
