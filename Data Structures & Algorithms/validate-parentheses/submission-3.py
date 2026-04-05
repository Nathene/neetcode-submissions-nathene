class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                    continue
    
            stack.append(c)
        
        return not stack
