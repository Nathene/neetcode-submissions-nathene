class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        times = len(hand) // groupSize
        def find_smallest() -> int:
            return min(count.keys())
        
        def prune():
            smallest = find_smallest()
            for _ in range(groupSize):
                if count.get(smallest, 0) > 0:
                    count[smallest] -= 1
                    if count[smallest] == 0:
                        count.pop(smallest)
                else:
                    return False
                smallest = smallest + 1
            return True
        
        for _ in range(times):
            if not prune():
                return False
        return not count