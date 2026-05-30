class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        first = [0] * 26
        second = [0] * 26
        for sc, tc in zip(s, t):
            s_ind, t_ind = ord(sc) - ord('a'), ord(tc) - ord('a')

            first[s_ind] += 1
            second[t_ind] += 1
        
        return first == second


