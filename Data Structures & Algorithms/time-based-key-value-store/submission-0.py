from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        closest = ""
        names = self.store[key]

        left, right = 0, len(names) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if names[mid][1] <= timestamp:
                closest = names[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return closest
            

