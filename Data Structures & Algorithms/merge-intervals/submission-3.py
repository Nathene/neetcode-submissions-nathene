from math import inf
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0]) # sort from the start O(NlogN)

        prev = -inf
        res = []

        for start, end in intervals:
            if start > prev:
                res.append([start, end])
                prev = max(prev, end)
            else: # start < prev
                prev = max(end, prev)
                res[-1][1] = prev




        return res



