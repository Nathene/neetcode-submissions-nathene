class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        heap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(heap, (count, char))
        
        while heap:
            count, char = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                count_two, char_two = heapq.heappop(heap)
                res += char_two
                count_two += 1
                if count_two:
                    heapq.heappush(heap, (count_two, char_two))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(heap, (count, char))

        
        return res
