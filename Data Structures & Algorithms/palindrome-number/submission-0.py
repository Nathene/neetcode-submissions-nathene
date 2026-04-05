class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # take off the rigt most element, 
        # use two pointers on the array

        num = []

        while x > 0:
            num.append(x % 10)
            x = x // 10
        
        l, r = 0, len(num) - 1

        while l < r:
            if num[l] != num[r]: return False
            l += 1
            r -= 1
        
        return True