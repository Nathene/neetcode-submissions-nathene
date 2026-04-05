class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        for c1, c2 in zip(word1, word2):
            res += c1
            res += c2
            i += 1
        
        if i < len(word1):
            res += word1[i:]
        if i < len(word2):
            res += word2[i:]

        return res