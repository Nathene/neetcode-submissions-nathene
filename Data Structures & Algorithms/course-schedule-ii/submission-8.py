from graphlib import TopologicalSorter, CycleError

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        res = []
        while queue:
            course = queue.popleft()
            res.append(course)

            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) == numCourses:
            return res
        
        return []