class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        res = []
        visiting = set()
        visited = set()
        def dfs(src: int) -> bool:
            if src in visiting:
                return False
            if src in visited:
                return True
            visiting.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            visited.add(src)
            visiting.remove(src)
            res.append(src)
            return res
        
        for i in range(n):
            if not dfs(i): return []
        
        return res[::-1]
        
        
        

            