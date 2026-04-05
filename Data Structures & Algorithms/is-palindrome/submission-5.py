class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        def isAlpha(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        while l < r:
            while not isAlpha(s[l]) and l < r:
                l += 1
            while not isAlpha(s[r]) and r > l:
                r -= 1
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True



