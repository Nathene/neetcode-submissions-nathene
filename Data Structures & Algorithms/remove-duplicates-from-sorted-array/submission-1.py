class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1

        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]


        return slow + 1


            