from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def solve(i: int):

            if i >= len(cost):
                return 0

            return cost[i] + min(solve(i+1), solve(i + 2))
        
        return min(solve(0), solve(1))


