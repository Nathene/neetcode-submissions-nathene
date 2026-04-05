class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], source: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for src, dst, wei in edges:
            adj[src].append((dst, wei))
        
        shortest = {}

        heap = [(0, source)]

        while heap:
            weight, node = heapq.heappop(heap)
            if node in shortest:
                continue
            
            shortest[node] = weight

            for nei, wei in adj[node]:
                if nei not in shortest:
                    heapq.heappush(heap, (wei + weight, nei))
            
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest