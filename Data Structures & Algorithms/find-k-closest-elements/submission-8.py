class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num:(abs(num - x)))
        return sorted(arr[:k])
        
        # find x in the array.

        # k times we should add in elements, say to a heap, this allows us to 
        # keep the sorted property for the result

        # find ele 
        # -> two pointer compare for heap k times
        # -> leave arr,
        # -> heappop k times

        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            else:
                r = m
                break
        
        heap = []
        l = r
        r = r + 1
        while True:
            if l < 0:
                heapq.heappush(heap, arr[r])
                r +=1
            elif r >= len(arr):
                heapq.heappush(heap, arr[l])
                l -= 1
            else:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    heapq.heappush(heap, arr[l])
                    l -= 1
                else:
                    heapq.heappush(heap, arr[r])
                    r +=1  
            
            if len(heap) == k:
                break
        
        res = []
        while heap:
            res.append(heapq.heappop(heap))
        
        return res
        


