class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in seen:
                return True
            seen.add(nums[r])

            if (r - l) >= k:
                seen.remove(nums[l])
                l += 1
            

        
        return False