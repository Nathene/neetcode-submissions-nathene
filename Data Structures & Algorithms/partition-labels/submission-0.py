class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start_and_end = { i:[float("inf"), float("-inf")] for i in range(26) }

        for i, c in enumerate(s):
            start_and_end[ord(c) - ord('a')][0] = min(start_and_end[ord(c) - ord('a')][0], i)
            start_and_end[ord(c) - ord('a')][1] = max(start_and_end[ord(c) - ord('a')][1], i)
        
        seen = set()
        res = []
        left = 0
        curr_max = 0
        for i, c in enumerate(s):
            curr_max = max(start_and_end[ord(c) - ord('a')][1], curr_max)

            if i == curr_max:
                res.append(i - left + 1)
                left = i + 1
            if c not in seen:
                seen.add(c)
        
        return res
                
            
