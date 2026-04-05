class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = [0] * 26, [0] * 26 # O(1) space

        for c in s:
            count_s[ord(c) - ord('a')] += 1
        
        for c in t:
            count_t[ord(c) - ord('a')] +=1
        
        return count_s == count_t # O(N * M) time where N and M are s and t