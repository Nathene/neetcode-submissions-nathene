class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0   
        freq = defaultdict(int)
        most_freq = -1
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most_freq = max(most_freq, freq[s[r]])

            while (r - l + 1) - most_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res

            
