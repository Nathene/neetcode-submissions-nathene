from graphlib import TopologicalSorter, CycleError

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ts = TopologicalSorter()
        
        for course in range(numCourses):
            ts.add(course)
        
        for crs, pre in prerequisites:
            ts.add(crs, pre)
        
        try:
            return list(ts.static_order())
        except CycleError:
            return []