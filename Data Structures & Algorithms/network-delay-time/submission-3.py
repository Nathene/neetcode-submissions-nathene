class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append([w, v])
        
        visit = set()
        visit.add(k)

        heap = [(0, k)]
        heapq.heapify(heap)

        while heap:
            wei, dst = heapq.heappop(heap)

            visit.add(dst)

            for w, nei in adj[dst]:
                if nei not in visit:
                    heapq.heappush(heap, [w + wei, nei])
            
            if len(visit) == n:
                return wei
        
        return -1


            
        