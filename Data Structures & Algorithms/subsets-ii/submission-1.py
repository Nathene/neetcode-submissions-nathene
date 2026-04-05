class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        def backtrack(start: startnt) -> None:
            res.append(curr[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return res

