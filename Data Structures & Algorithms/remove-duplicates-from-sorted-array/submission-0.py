class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        seen = set()
        while r < len(nums):
            
            while r < len(nums) -1 and nums[r] in seen:
                r += 1
            print(f'{l}, {r}')
            seen.add(nums[r])
            nums[l] = nums[r]
            l += 1
            r += 1

        return len(seen) 



                

