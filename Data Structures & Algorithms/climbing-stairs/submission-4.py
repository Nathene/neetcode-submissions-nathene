class Solution:
    def climbStairs(self, n: int) -> int:
        memo ={}

        def solve(i: int):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if i > n:
                return 0
            res = solve(i + 1) + solve(i + 2)
            memo[i] = res
            return memo[i]
        
        return solve(0)
