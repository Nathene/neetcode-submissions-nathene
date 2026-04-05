class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        res = 0

        for n in nums:
            res |= n
        
        return res * 2 ** (len(nums) - 1)


        def backtrack(i: int, curr: int) -> int:
            if i == len(nums):
                return curr
            
            return backtrack(i + 1, curr ^ nums[i]) + backtrack(i + 1, curr)


        return backtrack(0, 0)
            
