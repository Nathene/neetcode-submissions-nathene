class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)

        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        
        seen = set()
        q = deque([0])
        seen.add(0)


        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        
        return len(seen) == n
                
                

        