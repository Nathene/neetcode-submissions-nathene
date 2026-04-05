class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:        
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys or timestamp < self.keys[key][0][0]:
            return ""
        
        l, r = 0, len(self.keys[key]) - 1
        if timestamp >= self.keys[key][-1][0]:
            return self.keys[key][-1][1]

        while l < r:
            m = (l + r) // 2
            if self.keys[key][m][0] <= timestamp:
                l = m + 1
            else:
                r = m

        return self.keys[key][l - 1][1]