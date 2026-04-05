class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)

        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        dfs(0)
        
        return len(seen) == n
                
                

        