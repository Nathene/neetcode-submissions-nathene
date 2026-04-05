class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def solve(i: int) -> int:
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0

            res = cost[i] + min(solve(i + 1), solve(i + 2))
            
            memo[i] = res
            return res
        
        return min(solve(0), solve(1))
            
       