from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        levels = 0
        while r < len(nums) - 1:
            max_jump = 0
            for i in range(l, r + 1):
                max_jump = max(max_jump, nums[i] + i)
            l = r
            r = max_jump
            levels += 1
        
        return levels

