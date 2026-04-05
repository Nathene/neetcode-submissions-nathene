class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        t_count = Counter(t)
        window = defaultdict(int)
        have = 0
        # unique chars, not the sum. We do the check for have < need later.
        need = len(t_count)

        l = 0
        res, res_len = [-1, -1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in t_count and window[c] == t_count[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""


            
        
        

            
            





        