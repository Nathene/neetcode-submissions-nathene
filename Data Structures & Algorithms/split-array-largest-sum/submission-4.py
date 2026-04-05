class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def can_split(m: int) -> bool:
            curr = 0
            sub_count = 1
            for n in nums:
                curr += n
                if curr > m:
                    sub_count += 1
                    curr = n
            
            return sub_count <= k
        
        while l <= r:
            m = (l + r) // 2

            if can_split(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res


            

