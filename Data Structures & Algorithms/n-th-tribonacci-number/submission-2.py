class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def solve(i: int) -> int:
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            if i <= 2:
                return 1
            
            res = solve(i - 1) + solve(i-2) + solve(i-3)
            memo[i] = res
            return res
        
        return solve(n)
            

            

            