class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        for i, c in enumerate(s):
            last_index[c] = i
        
        print(last_index)
        
        res = []
        l, r = 0, 0
        for i, c in enumerate(s):
            r = max(r, last_index[c])
            if i == r:
                res.append(r - l +1)
                l = r + 1
                
        
        return res
            
            