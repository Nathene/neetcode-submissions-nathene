class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        # find the first char that isnt the same, 
        # minus that idnex from the length of the word. 
        l, r = 0, 0

        while r < len(s) and l < len(t):
            if t[l] == s[r]:
                l += 1
            
            r += 1
            if r == len(s):
                return len(t) - l
        
        return 0
            
            