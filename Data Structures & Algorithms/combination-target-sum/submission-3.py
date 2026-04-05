class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []

        def backtrack(i: int, rem: int) -> None:
            if rem == 0:
                res.append(curr[::])
                return
            if rem < 0 or i == len(nums):
                return
            
            curr.append(nums[i])
            backtrack(i, rem - nums[i])

            curr.pop()
            backtrack(i + 1, rem)
        
        backtrack(0, target)
        return res