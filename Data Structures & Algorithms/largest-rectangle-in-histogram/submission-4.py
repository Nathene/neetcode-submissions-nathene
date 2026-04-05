class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [7, 1, 7, 2, 2, 4]

        [[1, 0], [2, 2]]   ->   [4, 5]  
        2, 3, 4, 5 * 2 = 8
        
        max = 7 
        min_val = 2

        """
        n = len(heights)
        stack = [[heights[0], 0]]
        best = 0
        for r in range(1, len(heights)):
            start = r
            while stack and heights[r] <= stack[-1][0]:
                val, ind = stack.pop()
                start = ind
                best = max(best, (r - ind) * val, val)

            stack.append([heights[r], start])
        
        while stack:
            val, ind = stack.pop()
            best = max(best, (n - ind) * val)
        
        return best

            



