class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []

        freq = Counter(tasks)

        for key in freq:
            cycles = freq[key]
            heapq.heappush(heap, -cycles)
        

        time = 0
        q = deque() # holds [negative_remaining_cycles, available_time]

        while heap or q:
            time += 1

            if heap:
                cycles = heapq.heappop(heap)
                if cycles + 1 != 0:
                    q.append([cycles + 1, time + n])
            
            if q and q[0][1] <= time:
                cycles, _ = q.popleft()
                heapq.heappush(heap, cycles)

        return time
        
             

