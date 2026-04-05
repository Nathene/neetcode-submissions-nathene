class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []

        def backtrack(i: int) -> None:
            # base case
            if i == len(nums):
                res.append(curr[::])
                return
            
            # either add 
            curr.append(nums[i])

            backtrack(i + 1)

            # oor not add
            curr.pop()

            backtrack(i + 1)
        
        backtrack(0)
        return res
            