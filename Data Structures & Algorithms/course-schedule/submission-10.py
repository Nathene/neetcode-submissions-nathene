class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * (num_courses + 1)
        for crs, pre in prerequisites:
            in_degree[crs] += 1
            adj[pre].append(crs)

        q = deque([i for i in range(num_courses) if in_degree[i] == 0])
        courses_taken = 0
        while q:
            crs = q.popleft()
            courses_taken += 1
            for nei in adj[crs]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
                
        
        return True if courses_taken == num_courses else False