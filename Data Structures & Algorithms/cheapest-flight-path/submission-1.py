class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for s, d, wei in flights:
            adj[s].append([wei, d])

        heap = []
        for w, d in adj[src]:
            heapq.heappush(heap, [w, d, 0])
        while heap:
            wei, node, stops = heapq.heappop(heap)
            if node == dst:
                return wei
            if stops == k:
                continue
            for dist, nei in adj[node]:
                heapq.heappush(heap, [wei + dist, nei, stops + 1])

        return -1


            