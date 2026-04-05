class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        lookup = [0] * 26
        max_freq = 0

        for r in range(len(s)):
            lookup[ord(s[r]) - ord("A")] += 1

            max_freq = max(max_freq, lookup[ord(s[r]) - ord("A")])

            if (r - l + 1) - max_freq > k:
                lookup[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            res = max(res, (r - l) + 1)
        
        return res
            
     