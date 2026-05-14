class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for c1, c2 in zip(word1, word2):
            res += c1
            res += c2
        
        if len(word1) > len(word2):
            res += word1[len(word2):]
        elif len(word2) > len(word1):
            res += word2[len(word1):]
        
        return res