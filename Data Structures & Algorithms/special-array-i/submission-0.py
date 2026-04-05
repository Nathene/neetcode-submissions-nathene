class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        diff = nums[0] % 2
        for n in nums[1:]:
            if n % 2 == diff:
                return False
            diff = n % 2
        
        return True
