class Solution:
    def decodeString(self, s: str) -> str:
        stack = []


        for c in s:
            if c != "]":
                stack.append(c)
            else:
                sublist = []
                while stack[-1] != "[":
                    sublist.append(stack.pop())
                stack.pop()

                substr = "".join(reversed(sublist))

                amount = ""
                while stack and stack[-1].isdigit():
                    amount = stack.pop() + amount
                
                stack.append(int(amount) * substr)
        
        return "".join(stack)




