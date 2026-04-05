class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        curr = 0
        res = float("inf")
        while r < len(nums):
            curr += nums[r]

            while curr >= target and l <= r:
                res = min(res, (r - l + 1))
                curr -= nums[l]
                l += 1
            r += 1
        return res if res != float("inf") else 0

