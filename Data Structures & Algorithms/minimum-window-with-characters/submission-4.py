class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        window = defaultdict(int)
        have = 0
        need = len(count_t)
        res = s + s # can never be bigger than s

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while l < len(s) and have == need:
                if (r - l + 1) < len(res):
                    res = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1


        
        return res if len(res) <= len(s) else ""
            

