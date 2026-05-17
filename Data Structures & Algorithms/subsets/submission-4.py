class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        
        def backtrack(i: int) -> None:
            if i >= len(nums):
                res.append(curr[:])
                return
            
            # add to curr
            curr.append(nums[i])
            # recurse
            backtrack(i + 1)
            # pop from curr
            curr.pop()
            # recurse
            backtrack(i + 1)
        
        backtrack(0)
        return res