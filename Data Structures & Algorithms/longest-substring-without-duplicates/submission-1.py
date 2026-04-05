class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen = set()
        for r in range(len(s)):
            print(f"{len(set(s[l:r+1]))} == {len(s[l:r+1])}")
            if len(set(s[l:r+1])) == len(s[l:r+1]):
                res = max(res, (r - l) + 1)
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
        
        return res
            
                