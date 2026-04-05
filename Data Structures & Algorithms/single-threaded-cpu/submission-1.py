class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        res = []

        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort(key=lambda x:x[0])
        i, time = 0, tasks[0][0]   

        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]: # is it enque? 
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not heap:
                time = tasks[i][0]
            else:
                end, index = heapq.heappop(heap)
                time += end
                res.append(index)

        
        return res



            