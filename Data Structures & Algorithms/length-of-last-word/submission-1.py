class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.rstrip()

        r = len(s) - 1
        count = 0
        while s[r] == " ":
            r -= 1
        while s[r] != " " and r >= 0:
            r -= 1
            count += 1
        return count