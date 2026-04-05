class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        stack = []

        tmp = x
        length = 0
        while tmp >0:
            tmp  //= 10
            length += 1
        tmp = x
        for _ in range(length):
            stack.append(tmp%10)
            tmp //= 10
        
        while len(stack) > length // 2:
            if stack[-1] != x % 10:
                return False
            stack.pop()
            x//= 10
        
        return True
