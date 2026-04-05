class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        q = deque()

        count = Counter(tasks)
        for char, cnt in count.items():
            heapq.heappush(heap, (-cnt, char))
        print(heap)
        time = 0
        while heap or q:
            time += 1     
            if heap:
                count, char = heapq.heappop(heap)
                if count + 1 < 0:
                    q.append((time + n, count + 1, char))

            if q and q[0][0] <= time:
                _, count, char = q.popleft()
                heapq.heappush(heap, (count, char))

        
        return time