class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        curr = []
        nums.sort()
        def backtrack(i: int) -> None:
            if i == len(nums):
                res.append(curr[::])
                return
            
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()

            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(j)
        
        backtrack(0)
        return res
        
            



        backtrack(0)
        return res