class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def solve(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            rob = nums[i] + solve(i + 2)
            dont_rob = solve(i + 1)

            memo[i] = max(rob, dont_rob)
            return memo[i]
        
        return solve(0)
