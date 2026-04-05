class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for start, end, time in times:
            adj[start].append([time, end])
        seen =set([k])
        heap = [[0, k]]
        time = 0
        while heap:
            node = heapq.heappop(heap)
            seen.add(node[1])
            if len(seen) == n:
                return node[0]
            for time, nei in adj[node[1]]:
                if nei not in seen:
                    heapq.heappush(heap, [time + node[0], nei])
            

            
        return -1


            