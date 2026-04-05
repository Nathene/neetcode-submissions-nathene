class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ["+", "-", "/", "*"] and len(stack) > 1:
                b, a = int(stack.pop()), int(stack.pop())
                if t == "+": stack.append(a + b)
                if t == "-": stack.append(a - b)
                if t == "/": stack.append(int(a / b))
                if t == "*": stack.append(a * b)
            else:
                stack.append(int(t))
        
        return int(stack[0])