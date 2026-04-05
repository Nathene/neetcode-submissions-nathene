class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead_ends = set(deadends)
        if "0000" in dead_ends:
            return -1

        q = deque([("0000", 0)])
        visited = set("0000")
        while q:
            comb, changes = q.popleft()
            if comb == target:
                return changes

            for i in range(4):
                for move in [-1, 1]:
                    digit = (int(comb[i]) + move) % 10
                    next_comb = comb[:i] + str(digit) + comb[i+1:]
                    
                    if next_comb not in visited and next_comb not in dead_ends:
                        visited.add(next_comb)
                        q.append((next_comb, changes + 1))

        return -1