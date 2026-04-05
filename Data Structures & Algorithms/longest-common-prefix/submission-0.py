class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""

        for i in range(len(min(strs))):
            curr = strs[0][i] # first letter of first word
            for s in strs:
                if s[i] != curr:
                    return pre            
            pre += curr
        
        return pre