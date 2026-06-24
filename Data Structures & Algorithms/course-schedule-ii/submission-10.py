class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        adj_list: dict[int, list[int]] = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre_req in prerequisites:
            adj_list[pre_req].append(course)
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
