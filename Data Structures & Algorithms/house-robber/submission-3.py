class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        rob, dont_rob = nums[-1], max(nums[-1], nums[-2])

        for i in range(len(nums) - 3, -1, -1):
            new_val = max(nums[i] + rob, dont_rob)
            rob = dont_rob
            dont_rob = new_val
        
        return max(rob, dont_rob)