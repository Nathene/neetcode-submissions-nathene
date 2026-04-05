class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0

        for n in nums:
            curr = max(curr, 0)
            curr += n
            res = max(curr, res)
        
        return res