class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                b = stack[-1]
                a = stack[-2]
                stack.append(a + b)
            elif op == "C":
                if stack:
                    stack.pop()
            elif op =="D":
                if stack:
                    stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        
        return sum(stack)