from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def solve(i):
            if i >= n:
                return 0
            
            if 0 < n - i <= 2:
                return n - i

            return solve(i + 1) + solve(i + 2)
        
        return solve(0)