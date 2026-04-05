"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        heap = []

        for interval in intervals:
            start, end = interval.start, interval.end
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)


            
        
        return len(heap)



                        

        