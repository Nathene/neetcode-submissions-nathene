class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = defaultdict(list)

        for u, v, w in edges:
            adjList[u].append((w, v))
        

        heap = [(0, src)]
        seen = set()
        res = {}
        while heap:
            weight, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            res[node] = weight
            if len(seen) == n:
                break

            for wei, nei in adjList[node]:
                if nei not in seen:
                    heapq.heappush(heap, (wei + weight, nei))

        for i in range(n):
            if i not in seen:
                res[i] = -1     
        return res

    