# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        res = 1 if nums else 0
        for n in nums:
            if n - 1 in num_set:
                continue
            longest = 1
            while n + 1 in num_set:
                longest += 1
                res = max(res, longest)
                n += 1
        
        return res