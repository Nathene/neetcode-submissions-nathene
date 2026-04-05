from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def solve(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            res = solve(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                res += solve(i + 2)
            return res
        
        return solve(0)