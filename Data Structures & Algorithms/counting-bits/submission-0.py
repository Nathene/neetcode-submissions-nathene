class Solution:
    def countBits(self, n: int) -> List[int]:
        def num_ones(k: int) -> int:
            res = 0
            while k:
                res += k & 1
                k = k >> 1
            return res
        total = []
        for i in range(n+1):
            total.append(num_ones(i))
        
        return total