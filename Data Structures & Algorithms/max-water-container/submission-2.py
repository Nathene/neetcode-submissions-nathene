class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        l, r = 0, len(nums) - 1
        highest = -1
        while l < r:
            highest = max(highest, min(nums[l], nums[r]) * (r - l))
            if nums[l] > nums[r]:
                r -= 1
            else:
                l += 1
        
        return highest