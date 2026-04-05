from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def solve(i: int, end: int) -> int:
            if i >= end:
                return 0
            rob = nums[i] + solve(i + 2, end)
            not_rob = solve(i + 1, end)
            return max(rob, not_rob)
        
        return max(solve(0, len(nums) - 1), solve(1, len(nums)))
        
