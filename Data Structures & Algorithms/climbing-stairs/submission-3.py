from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def solve(i):
            if i >= n:
                return 0
            
            if n - i == 1:
                return 1
            if n - i == 2:
                return 2

            return solve(i + 1) + solve(i + 2)
        
        return solve(0)