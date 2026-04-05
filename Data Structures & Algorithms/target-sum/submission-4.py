class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(i: int, count: int) -> int:
            if (i, count) in memo:
                return memo[(i, count)]
            if i == len(nums):
                return 1 if count == target else 0
            
            add = dp(i + 1, count + nums[i])
            sub = dp(i + 1, count - nums[i])

            memo[(i, count)] = add + sub
            return memo[(i, count)]
        
        return dp(0, 0)