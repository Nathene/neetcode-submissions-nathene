class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        buckets = [0] * k
        total = sum(nums)
        want = total // k
        if want * k != total:
            return False
        
        nums.sort(reverse=True)
        if nums[0] > want: return False

        def backtrack(i: int) -> bool:
            if i == len(nums):
                return True
            
            for j in range(k):
                if buckets[j] + nums[i] <= want:
                    buckets[j] += nums[i]
                    if backtrack(i + 1): return True
                    buckets[j] -= nums[i]
                
                if buckets[j] == 0:
                    break
            
            return False
        
        return backtrack(0)