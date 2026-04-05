class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = "0000"
        if start in deadends:
            return -1

        q = deque([(start, 0)])
        visit = set(start)

        while q:

            comb, changes = q.popleft()

            if comb == target:
                return changes

            for i in range(4):
                for op in [-1, 1]:
                    digit = (int(comb[i]) + op) % 10
                    new_comb = comb[:i] + str(digit) + comb[i+1:]
                    if new_comb not in deadends and new_comb not in visit:
                        visit.add(new_comb)
                        q.append([new_comb, changes + 1])
            
                    
        return -1
