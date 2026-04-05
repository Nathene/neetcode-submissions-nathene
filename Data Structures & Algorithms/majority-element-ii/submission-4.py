class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)] 

        count = Counter(nums)

        for key, cnt in count.items():
            buckets[cnt].append(key)
        
        limit = len(nums) // 3
        res = []
        for i in range(limit + 1, len(buckets)):
            if buckets[i] == []: continue
            res.extend(buckets[i])
        return res