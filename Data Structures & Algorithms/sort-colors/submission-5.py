class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = Counter(nums)

        for i in range(len(nums)):
            if colors[0]:
                nums[i] = 0
                colors[0] -= 1
            elif colors[1]:
                nums[i] = 1
                colors[1] -= 1
            else:
                nums[i] = 2
        