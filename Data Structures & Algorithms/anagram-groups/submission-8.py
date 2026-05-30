class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            ana = [0] * 26
            for c in word:
                ind = ord(c) - ord('a')
                ana[ind] += 1
            
            groups[tuple(ana)].append(word)
        
        return list(groups.values())