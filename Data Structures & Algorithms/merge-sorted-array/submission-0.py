class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """ 
        for r in range(len(nums1) - 1, -1, -1):
            if n == 0:
                nums1[r] = nums1[m-1]
                m -= 1
                continue
            if m == 0:
                nums1[r] = nums2[n-1]
                n -= 1
                continue
            nums1[r] = max(nums2[n-1], nums1[m-1])
            if nums2[n-1] > nums1[m-1]:
                n -= 1
            else:
                m -= 1
        



        
                

