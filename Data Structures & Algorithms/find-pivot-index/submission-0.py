class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = []
        right = []
        prefix = 0
        for num in nums:
            prefix += num
            left.append(prefix)
        
        prefix = 0
        for i in range(len(nums) -1, -1, -1):
            prefix += nums[i]
            right.append(prefix)
        right.reverse()

        for i in range(len(nums)):
            left_sum = left[i-1] if i > 0 else 0
            right_sum = right[i+1] if i < len(nums) - 1 else 0
            if left_sum == right_sum:
                return i
        
        return -1
