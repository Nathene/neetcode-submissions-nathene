class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trip = [passengers, from, to]
        # 4: 1->2
        # 3: 2->4
        # True
        # prev_end <= new_start
        trips.sort(key=lambda x:x[1])

        curr_passengers = 0

        heap = []

        for trip in trips:
            passengers, start, end = trip
            while heap and heap[0][0] <= start:
                curr_passengers -= heap[0][1]
                heapq.heappop(heap)
            
            curr_passengers += passengers
            if curr_passengers > capacity:
                return False
            heapq.heappush(heap, [end, passengers])
        return True




