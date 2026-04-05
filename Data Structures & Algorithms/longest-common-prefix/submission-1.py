class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_char = ""
        res = ""
        for i in range(len(min(strs))):
            curr_char = strs[0][i]
            for word in strs:
                if word[i] != curr_char:
                    return res
            
            res += curr_char
        
        return res
                
