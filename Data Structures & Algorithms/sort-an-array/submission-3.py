class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        return self.merge_sort(0, len(nums) -1, nums)



    def merge_sort(self, l: int, r: int, arr: list[int]) -> list[int]:
        if l >= r:
            return arr
        m = (l + r) // 2
        self.merge_sort(l, m, arr)
        self.merge_sort(m + 1, r, arr)
        self.merge(l, m, r, arr)
        return arr
    
    def merge(self, l: int, m: int, r: int, arr: list[int]) -> None:
        left, right = arr[l:m+1], arr[m+1:r+1]
        i, lp, rp = l, 0, 0
        while lp < len(left) and rp < len(right):
            if left[lp] > right[rp]:
                arr[i] = right[rp]
                rp += 1
            else:
                arr[i] = left[lp]
                lp += 1
            i += 1
        while lp < len(left):
            arr[i] = left[lp]
            lp += 1
            i += 1
        while rp < len(right):
            arr[i] = right[rp]
            rp += 1
            i += 1