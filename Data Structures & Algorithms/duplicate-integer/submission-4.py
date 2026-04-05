class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        num_set = set(nums) # O(n) T
        return len(num_set) != len(nums)