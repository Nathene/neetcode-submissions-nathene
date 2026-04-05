class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, wei in edges:
            adj[src].append((dst, wei))
            adj[dst].append((src, wei))
        seen = set()
        heap = [[0, 0]]
        total = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)     
            total += weight

            for nei, wei in adj[node]:
                if nei not in seen:
                    heapq.heappush(heap, (wei, nei))
                

        if len(seen) != n:
            return -1

        return total

