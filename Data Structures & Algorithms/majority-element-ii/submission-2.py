class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums
        if not nums:
            return []
        nums.sort()
        res = []
        amount = len(nums) // 3
        curr = [nums[0], 1]
        added = set()
        for n in nums[1:]:
            print(curr, amount)
            if n == curr[0]:
                curr[1] += 1
            else:
                curr = [n, 1]
            if curr[1] > amount and curr[0] not in added:
                res.append(curr[0])
                added.add(curr[0])
            
        
        return res

            
        