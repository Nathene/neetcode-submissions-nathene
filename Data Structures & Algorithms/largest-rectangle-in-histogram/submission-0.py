# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
"""       
[ 7 ,1, 7, 2, 2, 4 ]

8

( 7, 2, 2, 4 ) 2 is the lowest height

[ 7 ,1, 7, 2, 2, 4 ]

Go through the array
capture the max, + compute the rectangles on the way

-> 7
-> 7, 2
-> 7, 3, 7
-> 7, 3, 7, 4
-> 7, 3, 7, 4, 6
-> 7, 3, 7, 4, 6, 8
return 8


[ 7#, 1#, 7, 2, 2, 4 ]

# Watcher variables
res = 7
lowest = 1
width 2

7 

"""
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # [index, height]
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, hei = stack.pop()
                res = max(res, hei * (i - ind))
                start = ind
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        
        return res



