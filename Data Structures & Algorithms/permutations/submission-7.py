# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
        
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        is_used = [False] * len(nums)

        def backtrack(path: list[int]) -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if is_used[i]:
                    continue
                is_used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                is_used[i] = False
        
        backtrack([])
        return res
                