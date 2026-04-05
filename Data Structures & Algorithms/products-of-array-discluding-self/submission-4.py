class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * (len(nums) + 1)
        backward = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            forward[i + 1] = nums[i] * forward[i]

        for i in range(len(nums) -1, -1, -1):
            backward[i] = nums[i] * backward[i + 1]
        
        res = []
        for i in range(len(nums)):
            res.append(forward[i] * backward[i + 1])
        
        return res
