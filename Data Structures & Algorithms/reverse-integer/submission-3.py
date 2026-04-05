class Solution:
    def reverse(self, x: int) -> int:
        rev = False
        if x < 0:
            rev = True
        
        res = 0
        upper_limit = 2 ** 31 - 1

        level = 1
        x = abs(x)

        tmp = x
        while tmp >= 10:
            level *= 10
            tmp //= 10
        while x > 0:
            val = x % 10
            if (val * level) > upper_limit: return 0
            res += (val * level)
            level //= 10
            x //= 10

        return -res if rev else res
