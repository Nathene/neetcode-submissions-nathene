class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = defaultdict(int)
        
        have = 0
        need = len(t)
        l = 0
        res = [-1, len(s)]

        for r in range(len(s)):
            char_r = s[r]
            if count_s[char_r] < count_t[char_r]:
                have += 1
            count_s[char_r] += 1

            while have == need:
                if (r - l) < (res[1] - res[0]):
                    res = [l, r]
                
                char_l = s[l]
                count_s[char_l] -= 1
                if count_s[char_l] < count_t[char_l]:
                    have -= 1
                l += 1  
        
        start, end = res
        return s[start : end + 1] if res[0] != -1 else ""