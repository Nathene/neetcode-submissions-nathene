class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        num_set = set(nums)
        return target in num_set