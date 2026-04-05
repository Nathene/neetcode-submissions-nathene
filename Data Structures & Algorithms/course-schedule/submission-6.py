"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
[crs, pre]
The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
n amount of nodes, in this graph
- assume we are given atleast 1 node, start at 0. 

Return true if it is possible to finish all courses, otherwise return false.
- if we find a cycle, return false

- we may need to pass through multiple nodes twice, this does not mean there is a cycle. 
e.g. 

    [1]
   /   \
[0] -- [2] -- [3] 
[0, 1], [0, 2], [1, 2], [2, 3]
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for crs, pre in prerequisites:
            adjlist[pre].append(crs)
        
        visit = set() 
        curr_path = set()

        def dfs(pre: int) -> bool:
            if pre in curr_path:
                return False
            if pre in visit:
                return True
            visit.add(pre)
            curr_path.add(pre)

            for nei in adjlist[pre]:
                if not dfs(nei): return False
            
            curr_path.remove(pre)
            return True
        
        for pre in range(numCourses):
            if not dfs(pre): return False
        
        return True
            