class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        if not intervals:
            return 0

        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        
        events.sort()
        res = 0
        curr = 0
        for event_time, diff in events:
            curr += diff
            res = max(res, curr)
        
        return res