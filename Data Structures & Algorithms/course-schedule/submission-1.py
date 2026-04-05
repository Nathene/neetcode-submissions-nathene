class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[pre].append(crs)

        seen = set()

        def dfs(crs: int) -> bool:
            if crs in seen:
                return False

            if adj[crs] == []:
                return True
            seen.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            seen.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
