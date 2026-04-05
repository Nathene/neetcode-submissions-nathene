class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [value, start]
        best = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                val, ind = stack.pop()
                best = max(best, (i - ind) * val)
                start = ind
            stack.append([h, start])
        n = len(heights)
        while stack:
            height, index = stack.pop()
            best = max(best, (n - index) * height)
        
        return best
