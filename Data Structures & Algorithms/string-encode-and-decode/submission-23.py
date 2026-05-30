class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f'{len(word)}#{word}'
        
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):
            amount = ""
            while s[i].isdigit():
                amount += s[i]
                i += 1
            i += 1
            words.append(s[i:i+int(amount)])
            i += int(amount)
        
        return words
            
