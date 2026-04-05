class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        where = { v:i for i, v in enumerate(nums1) }

        res = [-1] * len(nums1)
        stack = []

        for i, n in enumerate(nums2):
            while stack and stack[-1] < n:
                found = stack.pop()
                res[where[found]] = n
            if n in where:
                stack.append(n)
        
        return res
