class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # make an adj mapping pre -> crs
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[pre].append(crs)
        
        memo = {}
        def find(pre, target) -> bool:
            if (pre, target) in memo:
                return memo[(pre, target)]
            if pre == target:
                memo[(pre, target)] = True
                return True
            if adj[pre] == []:
                memo[(pre, target)] = False
                return False

            
            found = False
            for crs in adj[pre]:
                found = found or find(crs, target)
            
            
            memo[(pre, target)] = found
            return found

        # when we go through tre queries, we can just do a bfs on the course, and see if it exists
        res = []
        for crs, pre in queries:
            res.append(find(crs, pre))
        
        return res