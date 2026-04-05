class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = (l + r) // 2

            sqrt = m * m
            if sqrt > x:
                r = m - 1
            elif sqrt < x:
                l = m + 1
            else:
                return m
        
        return r