class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for word in strs:
            sorted_word = self.ordered_str(word)

            words[sorted_word].append(word)
        
        return list(words.values())
    
    def ordered_str(self, s: str) -> tuple[str]:
        res = [0] * 26

        for c in s:
            ind = ord(c) - ord('a')
            res[ind] += 1
        
        return tuple(res)