class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # what if you cant use the built in sort
        heapq.heapify(intervals)
        output = [heapq.heappop(intervals)]

        while intervals:
            start, end = heapq.heappop(intervals)
            prev_end = output[-1][1]

            if start <= prev_end:
                output[-1][1] = max(prev_end, end)
            else:
                output.append([start, end])

        return output



