# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [ [p, s] for p, s in zip(position, speed) ]

        pairs.sort(reverse=True)

        stack = []

        for p, s in pairs:
            reach = (target - p) / s
            if stack and reach <= stack[-1]:
                continue
            else:
                stack.append(reach)
        
        return len(stack)

# [ 1, 4 ]
# [ 3, 2 ]

# [ 4, 1 ] p
# [ 2, 3] s

# 10 - 4 / 1 = 6
# 10 - 2 / 3 = 

# 1 car pool