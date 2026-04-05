class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = [0] * 26, [0] * 26 # O(1) space

        for sc, tc in zip(s, t):
            count_s[ord(sc) - ord('a')] += 1
            count_t[ord(tc) - ord('a')] += 1
        
        return count_s == count_t and len(t) == len(s) # O(N * M) time where N and M are s and t