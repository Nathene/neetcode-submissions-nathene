class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        def backtrack(i: int) -> None:
            if i == len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[i])

            backtrack(i + 1)

            curr.pop()

            backtrack(i + 1)
        
        backtrack(0)
        return res