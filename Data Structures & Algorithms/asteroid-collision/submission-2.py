class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for c in asteroids:
            while stack and c < 0 and stack[-1] > 0:
                if abs(c) == stack[-1]:
                    stack.pop()
                    break
                elif abs(c) > stack[-1]:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(c)
        
        return stack