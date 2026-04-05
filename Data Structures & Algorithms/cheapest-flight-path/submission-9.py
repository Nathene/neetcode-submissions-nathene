class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        
        for start, end, weight in flights:
            adj[start].append((weight, end))
        
        min_cost = float("inf")

        q = deque([(0, 0, src)])
        dist = [float("inf")] * n
        dist[src] = 0
        
        while q:
            weight, stops, node = q.popleft()
            
            if node == dst:
                min_cost = min(min_cost, weight)
                continue
            if stops > k:
                continue
            
            for wei, nei in adj[node]:
                new_cost = wei + weight
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    q.append([new_cost, stops + 1, nei])

        
        return min_cost if min_cost != float("inf") else -1