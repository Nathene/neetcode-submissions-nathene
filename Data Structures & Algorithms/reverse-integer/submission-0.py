class Solution:
    def reverse(self, x: int) -> int:
        rev = False
        if x < 0:
            rev = True
        
        upper = 2 ** 31 - 1
        lower = -upper

        if rev:
            res = -int(str(abs(x))[::-1])
            if res < lower: return 0
            return res
        else:
            res = int(str(x)[::-1])
            if res > upper:
                return 0
            return res
