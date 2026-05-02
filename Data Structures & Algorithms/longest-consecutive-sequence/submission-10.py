class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0
        for num in nums:
            if num - 1 in  num_set:
                continue
            curr = num
            curr_window = 0
            while curr in num_set:
                curr += 1
                curr_window += 1
            
            best = max(best, curr_window)
        
        return best