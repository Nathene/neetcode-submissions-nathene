class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high = 0, len(nums) - 1
        curr = 0
        while curr <= high:
            if nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                low += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1
            else:
                curr += 1
        

            
        

        
        
        
        
        # colors = Counter(nums)

        # for i in range(len(nums)):
        #     if colors[0]:
        #         nums[i] = 0
        #         colors[0] -= 1
        #     elif colors[1]:
        #         nums[i] = 1
        #         colors[1] -= 1
        #     else:
        #         nums[i] = 2
        # O(N) time, O(N) space


        