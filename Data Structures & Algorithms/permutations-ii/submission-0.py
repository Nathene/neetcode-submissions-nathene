class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        used = [False] * len(nums)
        def backtrack() -> None:
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i-1] and not used[i - 1]: continue
                
                used[i] = True
                curr.append(nums[i])
                backtrack()
                curr.pop()
                used[i] = False

        backtrack()
        return res