# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        res= 0
        for n in nums:
            longest = 1

            while n + 1 in num_set:
                longest += 1
                n += 1
            res = max(res, longest)
        return res