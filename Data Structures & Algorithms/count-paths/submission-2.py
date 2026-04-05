
from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = n
        cols = m
        
        @cache
        def solve(r, c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            
            return (solve(r + 1, c) + solve(r, c + 1))
        

        return solve(0, 0)
