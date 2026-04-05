class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        
        def backtrack(path):
            # Base case: if our current path is full, we found a permutation
            if len(path) == len(nums):
                res.append(path[:]) # Copy the path
                return
            
            for i in range(len(nums)):
                # Skip if we've already picked this number for our path
                if used[i]:
                    continue
                
                # 1. Action: Choose the number and mark it used
                used[i] = True
                path.append(nums[i])
                
                # 2. Recurse: Go deeper to pick the next number
                backtrack(path)
                
                # 3. Backtrack: Undo the choice for the next loop iteration
                path.pop()
                used[i] = False
        
        backtrack([])
        return res