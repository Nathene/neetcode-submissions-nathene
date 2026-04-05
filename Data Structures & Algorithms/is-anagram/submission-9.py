class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = [0] * 26
        count_t = [0] * 26

        for sc, tc in zip(s, t):
            count_s[ord(sc) - ord('a')] += 1
            count_t[ord(tc) - ord('a')] += 1
        
        return count_s == count_t and len(s) == len(t)
            