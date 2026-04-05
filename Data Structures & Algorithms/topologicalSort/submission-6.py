class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        res = []
        q = deque()
        for i, deg in enumerate(in_degree):
            if deg == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
            
        return res if len(res) == n else []


        
        
        

            