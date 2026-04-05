class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for key, cnt in count.items():
            if cnt > len(nums) // 3:
                res.append(key)
        
        return res