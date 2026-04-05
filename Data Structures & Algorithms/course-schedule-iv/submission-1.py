from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # make an adj mapping pre -> crs
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[pre].append(crs)
        
        @cache
        def find(pre, target) -> bool:
            if pre == target:
                return True
            if adj[pre] == []:
                return False
            
            found = False
            for crs in adj[pre]:
                found = found or find(crs, target)
            
            return found

        # when we go through tre queries, we can just do a bfs on the course, and see if it exists
        res = []
        for crs, pre in queries:
            res.append(find(crs, pre))
        
        return res