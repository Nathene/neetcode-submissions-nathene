class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        heap = [(-cnt, char) for char, cnt in count.items()]
        res = []
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if q and q[0][0] <= time:
                _, count, char = q.popleft()
                heapq.heappush(heap, (count, char))
            
            if not heap:
                return ""

            curr_count, char = heapq.heappop(heap)
            res.append(char)
            if curr_count + 1 < 0:
                q.append((time + 2, curr_count + 1, char))
            
        return "".join(res)


        
