from graphlib import TopologicalSorter, CycleError

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        ts = TopologicalSorter()

        for course in range(numCourses):
            ts.add(course)
        
        for course, prereq in prerequisites:
            ts.add(course, prereq)
        
        try:
            return list(ts.static_order())
        except:
            return []