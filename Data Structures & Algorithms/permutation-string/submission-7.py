class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        for c in s1:
            count_s1[c] += 1

        count_s2 = defaultdict(int)

        l, r = 0, 0
        while r < len(s2):
            count_s2[s2[r]] += 1
            if (r - l) > len(s1) - 1:
                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0: del count_s2[s2[l]]
                l += 1

            
            if count_s2 == count_s1:
                return True
        
            r += 1
        
        return False
