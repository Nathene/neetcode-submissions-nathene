class Solution:
    def isValid(self, s: str) -> bool:
        paren = { "]": '[', "}": "{", ")": "(" }
        stack = []
        for c in s:
            if c in paren and stack and stack[-1] == paren[c]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0 