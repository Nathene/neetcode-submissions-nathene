class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                left, right, mid = nums[l], nums[r], nums[i]

                if left + right + mid > 0:
                    r -= 1
                elif left + right + mid < 0:
                    l += 1
                else:
                    if [left, mid, right] not in res:
                        res.append([left, mid, right])
                    l += 1
                    r -= 1
        
        return res



    

        