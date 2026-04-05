class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_to_index = { v:i for i, v in enumerate(nums1) }

        res = [-1] * len(nums1)
        stack = []

        for i, n in enumerate(nums2):
            while stack and stack[-1] < n:
                val = stack.pop()
                res[val_to_index[val]] = n
            if n in val_to_index:
                stack.append(n)
        
        return res
