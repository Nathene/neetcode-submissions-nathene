class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(queries[i], i) for i in range(len(queries))]
        intervals.sort()
        interval_index = 0
        heap = []
        res = [-1] * len(queries)

        for query in sorted(queries):
            while interval_index < len(intervals) and intervals[interval_index][0] <= query[0]:
                start, end = intervals[interval_index]
                heapq.heappush(heap, (end - start + 1, end))
                interval_index += 1
            
            while heap and heap[0][1] < query[0]:
                heapq.heappop(heap)
            
            if heap:
                res[query[1]] = heap[0][0]
        
        return res






