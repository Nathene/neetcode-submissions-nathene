class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            while r >= l and nums[r] == val:
                r -= 1
            if l <= r and nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif l <= r:
                l += 1
        
        return l