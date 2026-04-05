class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



        # two pointers, result variable to caclulate the current max

        
        # go through the list, sliding window, and keep the max increasing in result

        # return the result