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

        intervals.sort(key=lambda x: x.start)

        active_rooms = []
        heapq.heappush(active_rooms, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= active_rooms[0]:
                heapq.heappop(active_rooms)

            heapq.heappush(active_rooms, intervals[i].end) 
        
        return len(active_rooms)
       

            
