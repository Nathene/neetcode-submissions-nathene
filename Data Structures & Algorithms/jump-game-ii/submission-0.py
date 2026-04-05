from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def solve(i: int) -> int:
            if i >= len(nums) - 1:
                return 0

            res = float("inf")
            for j in range(1, nums[i] + 1):
                res = min(res, 1 + solve(j + i))
            
            return res
        
        res = solve(0)
        return res if res != float("inf") else -1
