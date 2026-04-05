"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        prev_end = intervals[0].end if intervals else 0
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if start >= prev_end:
                prev_end = end
            else:
                return False
        
        return True
