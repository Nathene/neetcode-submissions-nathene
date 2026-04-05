class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        res = 0
        if not nums:
            return 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
                res += 1
            
            
        return res

