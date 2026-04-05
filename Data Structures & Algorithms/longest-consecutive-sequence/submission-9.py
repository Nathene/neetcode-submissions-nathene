class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for n in nums:
            if n - 1 in num_set: continue
            curr = 0
            j = n
            while j in num_set:
                curr += 1
                j += 1
            
            res = max(res, curr)
        
        return res