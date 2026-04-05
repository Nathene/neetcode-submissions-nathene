class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [val, index]
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([v, i])
        
        return res