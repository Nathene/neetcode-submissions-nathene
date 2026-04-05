class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1

        while l <= r:
            curr_max = min(heights[l], heights[r]) * (r - l)
            res = max(res, curr_max)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
