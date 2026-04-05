class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        for crs, pre in prerequisites:
            adjlist[pre].append(crs)
        
        visit = [0] * numCourses
        res = []
        def dfs(pre: int) -> bool:
            if visit[pre] == 1:
                return False
            if visit[pre] == 2:
                return True
        
            visit[pre] = 1
            for nei in adjlist[pre]:
                if not dfs(nei): return False
            visit[pre] = 2
            res.append(pre)

            return True
        
        for pre in range(numCourses):
            if not dfs(pre):
                return []
        
        return res[::-1]
            