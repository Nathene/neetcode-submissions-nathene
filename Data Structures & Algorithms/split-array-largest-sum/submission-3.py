from functools import cache
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i: int, m: int) -> int:
            if m == 1:
                return sum(nums[i:])
            
            res, curr_sum = float("inf"), 0
            for j in range(i, len(nums) - m + 1):
                curr_sum += nums[j]
                max_sum = max(curr_sum, dfs(j + 1, m - 1))
                res = min(res, max_sum)

            
            return res
        
        return dfs(0, k)

