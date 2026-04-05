from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def solve(i: int) -> int:

            if i >= len(nums):
                return 0
            
            # other wise, choose to rob
            rob = nums[i] + solve(i + 2)
            # or not rob
            not_rob = solve(i + 1)

            return max(rob, not_rob)
        
        return solve(0)