"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        events = [] # [time: int, in_meeting: bool]

        for meeting in intervals:
            events.append([meeting.start, True])
            events.append([meeting.end, False])
        
        events.sort()
        rooms = 0
        for time, in_meeting in events:
            if in_meeting:
                rooms += 1
            else:
                rooms -= 1
            res = max(res, rooms)
        
        return res
            