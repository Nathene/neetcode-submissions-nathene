class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        res = []
        seen = {}
        def dfs(src: int) -> bool:
            if src not in seen:
                seen[src] = True
            elif seen[src] == False:
                return True
            else:
                return False

            for nei in adj[src]:
                if not dfs(nei):
                    return False
            
            seen[src] = False
            res.append(src)

            return res
        
        for i in range(n):
            if not dfs(i): return []
        
        return res[::-1]
        
        
        

            