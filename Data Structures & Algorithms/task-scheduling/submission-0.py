import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = [ -ele for ele in count.values() ]
        heapq.heapify(heap)
        q = deque() # [-ele, when_ready]
        time = 0

        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap) # [-ele + 1]
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time











            
            


