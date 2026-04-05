class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26  
        max_freq = 0
        res = 0
        l = 0

        for r in range(len(s)):
            char_count[(ord(s[r]) - ord("A"))] += 1
            max_freq = max(max_freq, char_count[(ord(s[r]) - ord("A"))])

            while ((r - l + 1) - max_freq) > k:
                char_count[(ord(s[l]) - ord("A"))] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
            
        return res
