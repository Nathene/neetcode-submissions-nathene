class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        one, two = nums[-1], max(nums[-1], nums[-2])

        for i in range(len(nums) - 3, -1, -1):
            new_val = max(nums[i] + one, two)
            one = two
            two = new_val
        
        return max(one, two)