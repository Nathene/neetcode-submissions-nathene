class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        edge_cnt = {}
        leaves = deque()
        for src, nei in adj.items():
            if len(nei) == 1:
                leaves.append(src)
            edge_cnt[src] = len(nei)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
        
        return [0]





            

            
        


        # adj = defaultdict(list)
        # for start, end in edges:
        #     adj[start].append(end)
        #     adj[end].append(start)

        # def bfs(i: int) -> int:
        #     q = deque([(i, 1)])

        #     visit = set()
        #     res = 0
        #     while q:
        #         new_root, level = q.popleft()
        #         visit.add(new_root)
        #         res = level
        #         for nei in adj[new_root]:
        #             if nei not in visit:
        #                 q.append([nei, level + 1])

        #     return res  

        # smallest = n
        # for i in range(n):
        #     smallest = min(smallest, bfs(i))
        # res = []
        # for i in range(n):
        #     if bfs(i) == smallest:
        #         res.append(i)
        
        # return res
        
            
