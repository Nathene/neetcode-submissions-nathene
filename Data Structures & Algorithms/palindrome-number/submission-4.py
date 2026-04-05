class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        tmp = x
        length = 0
        while tmp > 0:
            tmp //= 10
            length += 1
        
        res = 0
        if length % 2 == 0:
            while x > 0:
                res ^= x % 10
                x //= 10
            return res == 0

        i = 1
        target = 0
        while x > 0:
            curr = x % 10
            if i == (length + 1) // 2:
                target = curr
            res ^= curr
            i += 1
            
            x //= 10
            
        return res == target





        

        # now we collect the numbers into a stack and compare.