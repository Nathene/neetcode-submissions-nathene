class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        memo = {}
        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1

            
            res = 0

            res += dfs(r + 1, c)
            res += dfs(r, c + 1)

            memo[(r, c)] = res
            return res
        
        return dfs(0, 0) 
        