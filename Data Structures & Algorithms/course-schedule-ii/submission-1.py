class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        seen = set()
        cycle = set()
        res = []
        def dfs(pre: int) -> bool:
            if pre in cycle:
                return False
            if pre in seen:
                return True
            cycle.add(pre)
            for crs in adj[pre]:
                if not dfs(crs): return False
            cycle.remove(pre)
            seen.add(pre)
            res.append(pre)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res[::-1]
