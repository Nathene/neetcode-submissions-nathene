"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)

        heap = []

        for i in intervals:
            
            if heap and heap[0] <= i.start:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
        return len(heap)

        