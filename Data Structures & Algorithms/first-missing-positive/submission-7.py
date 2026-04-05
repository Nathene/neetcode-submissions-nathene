class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # loop through the array once, 
        # if we find a number, and its within the bounds of 1..n
        # update the index - 1 of the array to be inf
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0

        for i, n in enumerate(nums):
            val = abs(n)

            if 0 < val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        # second pass, we go from 1..n, check at the index of the array to see what is there.
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i 
        
        return len(nums) + 1