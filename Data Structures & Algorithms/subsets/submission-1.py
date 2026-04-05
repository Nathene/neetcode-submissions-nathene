class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []

        def backtracking(i: int) -> None:
            if i == len(nums):
                res.append(curr[::])
                return
            
            curr.append(nums[i])

            backtracking(i + 1)

             # OR
            
            curr.pop()

            backtracking(i + 1)
        
        backtracking(0)

        return res