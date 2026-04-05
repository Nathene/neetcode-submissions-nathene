class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        completed = set()
        cycle = set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in completed:
                return True
            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            adj[crs] = []
            cycle.remove(crs)
            completed.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res[::-1]