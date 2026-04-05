class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd case
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            # even case
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        
        return res


