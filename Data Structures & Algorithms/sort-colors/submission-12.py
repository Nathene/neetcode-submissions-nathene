class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for n in nums:
            colors[n] += 1

        i = 0
        for ind, c in enumerate(colors):
            while c > 0:
                nums[i] = ind
                c -= 1
                i += 1

