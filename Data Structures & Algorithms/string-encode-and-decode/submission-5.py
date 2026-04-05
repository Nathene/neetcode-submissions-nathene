class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f"{len(word)}#{word}")
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            amount = ""
            while i < len(s) and s[i].isdigit():
                amount += s[i]
                i += 1
            int_amount = int(amount)

            word = s[i + 1: i + 1 + int_amount]  # i + 1 == "#"
            res.append(word)
            i += int_amount + 1
        
        return res
