# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a hashset, 
        # iterate through the array
        # see if we have a number that is -1 or + 1 from that in the set 
        # using a while loop
        # record the max amount of consecutive numbers.
        num_set = set(nums)
        seen = set()
        total = 0
        for i in range(len(nums)):
            curr = 1
            can_pos = nums[i] + 1
            can_neg = nums[i] - 1
            while can_pos in num_set:
                if can_pos in seen:
                    break
                curr += 1
                seen.add(can_pos)
                can_pos += 1
                
            while can_neg in num_set:
                if can_pos in seen:
                    break
                curr += 1
                seen.add(can_neg)
                can_neg -= 1
                
            total = max(total, curr)


        return total