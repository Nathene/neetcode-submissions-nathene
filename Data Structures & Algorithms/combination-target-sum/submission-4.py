class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i: int, curr: int, path: list[int]):
            if curr == target:
                res.append(path[:])
                return
            
            if curr > target or i == len(nums):
                return
            
            backtrack(i, curr + nums[i], path + [nums[i]])

            backtrack(i + 1, curr, path)

        backtrack(0, 0, [])
        return res