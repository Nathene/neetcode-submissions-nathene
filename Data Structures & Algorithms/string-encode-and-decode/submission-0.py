class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ""
        for string in strs:
            finalStr += string + "#!"
        
        return finalStr


    def decode(self, s: str) -> List[str]:
        result = s.split("#!")
        if result[-1] == "":
            result = result[:-1]
        return result

