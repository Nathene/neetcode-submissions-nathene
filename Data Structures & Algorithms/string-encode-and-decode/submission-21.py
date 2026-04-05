class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i) # find(character, start*, end*) -> * denotes optional
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            i = j + length
        
        return res
            
