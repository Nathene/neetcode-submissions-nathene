from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        seen = set()

        def dfs(crs: int) -> bool:
            if crs in seen:
                return False
            if adj[crs] == []:
                return True
            
            seen.add(crs)

            for nei in adj[crs]:
                if not dfs(nei): return False
            
            seen.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            
            
