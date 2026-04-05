class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = { "*", "+", "-", "/" }



        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue
            right, left = stack.pop(), stack.pop()
            if t == "*":
                stack.append(left * right)
            elif t == "+":
                stack.append(left + right)
            elif t == "-":
                stack.append(left - right)
            elif t == "/":
                stack.append(int(left / right))
            
        
        return stack[-1]