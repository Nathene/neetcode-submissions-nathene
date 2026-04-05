class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0]) # sort from the start interval
                                                         # O(NlogN) Time
        total = 0
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev:
                prev = end
            else:
                total += 1
                prev = min(prev, end)
        
        return total
                # we have a conflict
                

