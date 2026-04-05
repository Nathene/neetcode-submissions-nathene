class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        def calc_avg(sub):
            return sum(sub) // len(sub)

        l = 0
        res = 0
        for r in range(k - 1, len(arr)):
            if calc_avg(arr[l:r + 1]) >= threshold:
                res += 1
            l += 1
        return res
