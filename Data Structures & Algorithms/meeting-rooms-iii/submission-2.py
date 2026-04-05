class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [i for i in range(n)]
        cooldown = []
        meetings.sort()
        count = [0] * n

        for i in range(len(meetings)):
            start, end = meetings[i]
            
            while cooldown and cooldown[0][0] <= start:
                _, room = heapq.heappop(cooldown)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(cooldown, [end, room])
            else:
                free_time, room = heapq.heappop(cooldown)
                duration = end - start
                count[room] += 1
                heapq.heappush(cooldown, [free_time + duration, room])
        
        return count.index(max(count))
