"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        sweep_line = []
        for interval in intervals:
            sweep_line.append([interval.start, "start"])
            sweep_line.append([interval.end, "end"])
        
        sweep_line.sort(key=lambda x:(x[0], x[1]))

        total = 0
        res = 0
        for time, i_type in sweep_line:
            if i_type == "start":
                total += 1
            else:
                total -= 1
            res = max(res, total)
        
        return res
       

            
