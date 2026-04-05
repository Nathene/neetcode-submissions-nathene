class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_ele = 0
        result = 0
        for key, amount in Counter(nums).items():
            max_ele = max(max_ele, amount)
            if max_ele == amount:
                result = key
        return result