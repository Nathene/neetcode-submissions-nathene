from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @cache
        def solve(i: int) -> bool:
            if i == len(nums) - 1: return True
            if nums[i] == 0: return False

            found = False
            for jump in range(1, nums[i] + 1):
                found = found or solve(jump + i)
            
            return found
        
        return solve(0)
