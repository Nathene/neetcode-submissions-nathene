from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        @cache
        def solve(r: int, c: int) -> int:
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            
            down = solve(r +1, c)
            right = solve(r, c + 1)

            return down + right
        
        return solve(0, 0)
