class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        num_set = set(nums)

        for num in nums:
            if num - 1 in num_set: continue

            curr = 1
            new_num = num + 1
            while new_num in num_set:
                curr += 1
                new_num += 1
            
            longest = max(longest, curr)
        
        return longest