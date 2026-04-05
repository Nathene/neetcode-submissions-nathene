class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        new_slow = 0

        while True:
            slow = nums[slow]
            new_slow = nums[new_slow] 

            if slow == new_slow:
                return slow
            



        
"""
You are given an array of integers nums containing n + 1 integers. Each integer 
in nums is in the range [1, n] inclusive.

# key node is 1-n inclusive

Every integer appears exactly once, except for one integer which appears two or more times. 
Return the integer that appears more than once.
"""