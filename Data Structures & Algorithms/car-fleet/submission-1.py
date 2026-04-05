# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))

        pairs.sort(reverse=True) # by default will sort this correctly
        # otherwise we can do: pairs.sort(key=lambda x:x[0], reverse=True)

        stack = []

        for pos, spe in pairs:
            arrival = (target - pos) / spe

            if stack and stack[-1] >= arrival:
                continue
            else:
                stack.append(arrival)
        
        return len(stack)