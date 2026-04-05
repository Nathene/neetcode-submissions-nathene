class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [num for num in nums]

        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                num *= nums[j]
            res[i] = num
        
        return res
                