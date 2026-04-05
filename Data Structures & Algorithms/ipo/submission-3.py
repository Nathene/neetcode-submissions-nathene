class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = list(zip(capital, profits))
        pairs.sort()

        heap = []
        i = 0
    

        while heap or i < len(pairs):
            # get the latest capital, 
            while i < len(pairs) and pairs[i][0] <= w: # capital is purchasable
            # add that into the best profits
                heapq.heappush(heap, [-pairs[i][1], pairs[i][0]])
                i += 1

            if not heap:
                i = pairs[i][1]
                continue
            # do that k times
            profit, capital = heapq.heappop(heap)
            w += abs(profit)
            k -= 1
            
            if k == 0:
                break
        
        return w

