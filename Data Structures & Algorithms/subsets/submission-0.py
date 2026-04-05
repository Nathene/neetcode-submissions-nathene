class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def sub(i):
            if i == len(nums):
                res.append(curr[::])
                return
            
            curr.append(nums[i])
            sub(i + 1)
            curr.pop()
            sub(i +1)
            
            


  

        sub(0)
        return res