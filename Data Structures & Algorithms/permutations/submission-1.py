class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, start):
            if start == len(nums):
                res.append(arr[::])
                return
            
            for i in range(start, len(arr)):
                arr[start], arr[i] = arr[i], arr[start]
                backtrack(arr, start + 1)
                arr[start], arr[i] = arr[i], arr[start]

        backtrack(nums, 0)
        return res