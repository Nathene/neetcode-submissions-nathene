class Solution:
    def reverse(self, x: int) -> int:
        rev = False
        if x < 0:
            rev = True
        
        upper_limit = 2 ** 31 - 1
        # Lower limit is -2**31, but since we work with abs(x), 
        # we handle the range overflow check carefully.

        res = 0
        x = abs(x)
        while x > 0:
            pop = x % 10
            x //= 10
            
            # Check overflow before multiplying by 10 and adding pop
            if res > (upper_limit // 10):
                return 0
            if res == (upper_limit // 10) and pop > 7:
                return 0
                
            res = res * 10 + pop

        return -res if rev else res