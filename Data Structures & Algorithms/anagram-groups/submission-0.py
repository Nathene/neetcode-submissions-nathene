class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)

        for ele in strs:
            sortedString = "".join(sorted(ele))
            d[sortedString].append(ele)
        return list(d.values())
        