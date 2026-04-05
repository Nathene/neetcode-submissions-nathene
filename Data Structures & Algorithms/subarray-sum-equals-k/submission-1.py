class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curr_sum = 0

        prefix = { 0 : 1 }

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefix.get(diff, 0)
            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)
        
        return res

        # { 0: 1 }
        # 2 - k == 2-2 = 0
        # count[0] = 1
        # res +=1 
        # count[2] += 1
        # { 0: 1, 2: 1 }
        # 2-1 = 1, count[1] == 0, so res stays
        # { 0: 1, 2: 1, 1: 1 }
        # 1 + 1 == 2, count[2] == 1
        # res += 1
        # count[2] += 1 
        # { 0: 1, 2: 2, 1: 1 }
        # 2 - k == 2 again
        # res += count[2] = 2


