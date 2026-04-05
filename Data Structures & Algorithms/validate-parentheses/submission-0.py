class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = collections.defaultdict(str)
        pairs[')'] = '('
        pairs[']'] = '['
        pairs['}'] = '{'
        for c in s:
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return stack == []
