class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
  
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                sub_str = ""
                while stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                stack.pop()

                amount = ""
                while stack and stack[-1].isdigit():
                    amount = stack.pop() + amount
                
                stack.append(int(amount) * sub_str)
        return "".join(stack)
                
