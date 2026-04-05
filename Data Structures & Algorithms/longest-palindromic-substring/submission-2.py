class Solution:
    def longestPalindrome(self, s: str) -> str:
        res= ""

        for i in range(len(s)):

            # handle the even case
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if (r - l) > len(res):
                res = s[l+1:r]

            # handle the odd case
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if (r - l) > len(res):
                res = s[l+1:r]
        
        return res
            