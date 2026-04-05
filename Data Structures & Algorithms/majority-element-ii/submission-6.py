class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)] 

        count = Counter(nums)
        res = []
        for key, cnt in count.items():
            if cnt > len(nums) // 3:
                res.append(key)
        
        return res