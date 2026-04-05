class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            word_count = [0] * 26
            for c in word:
                word_count[ord(c) - ord("a")] += 1
            res[tuple(word_count)] = res.get(tuple(word_count), [])
            res[tuple(word_count)].append(word)
        
        return list(res.values())
