class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # top down DP memoization approach
        memo = {}
        def solve(i: int, cap: int) -> int:
            if (i, cap) in memo:
                return memo[(i, cap)]
            if i >= cap: # out of bounds
                return 0
            
            rob = nums[i] + solve(i + 2, cap)
            dont_rob = solve(i + 1, cap)
            memo[(i, cap)] = max(rob, dont_rob)
            return memo[(i, cap)]

        return max(solve(0, len(nums) - 1), solve(1, len(nums)))
            
            