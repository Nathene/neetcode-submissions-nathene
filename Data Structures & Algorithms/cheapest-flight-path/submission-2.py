class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, wei in flights:
            adj[s].append((d, wei))
        
        # Optimization: Track the minimum stops to reach each node
        # This prevents the E * 2^k complexity
        stop_count = [float('inf')] * n
        
        # heap: [cost, current_node, stops_made]
        heap = [(0, src, 0)]
        
        while heap:
            cost, u, stops = heapq.heappop(heap)
            
            # If we've reached the destination, this MUST be the cheapest 
            # because of the Min-Heap property.
            if u == dst:
                return cost
            
            # If we've already visited this node with fewer or equal stops, 
            # there's no point in exploring further from here.
            if stops > k or stops >= stop_count[u]:
                continue
            
            # Update the best stop count for this node
            stop_count[u] = stops
            
            for v, weight in adj[u]:
                heapq.heappush(heap, (cost + weight, v, stops + 1))
                
        return -1