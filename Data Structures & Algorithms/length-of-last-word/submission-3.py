class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.rstrip(" ")
        r = len(s) - 1
        while r > 0 and s[r] == " ":
            r -= 1
        
        res = 0
        while r >= 0 and s[r] != " ":
            r -= 1
            res += 1

        return res