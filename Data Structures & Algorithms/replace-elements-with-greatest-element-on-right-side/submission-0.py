class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        max_val = arr[-1]
        arr.pop()
        for i, v in enumerate(arr[::-1]):
            arr[i] = max_val
            max_val = max(max_val, v)

        
        return arr[::-1] + [-1]

