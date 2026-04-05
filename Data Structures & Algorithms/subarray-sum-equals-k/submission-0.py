from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        counts = defaultdict(int)
        counts[0] = 1

        curr_sum = 0
        for n in nums:
            curr_sum += n
            res += counts[curr_sum - k]
            counts[curr_sum] += 1
            
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
        # res =  

