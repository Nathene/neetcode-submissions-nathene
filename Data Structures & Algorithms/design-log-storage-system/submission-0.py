class LogSystem:
    def __init__(self):
        self.logs = [] # Stores tuples of (raw_string, id)

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        # Map out exactly where each time unit cuts off in the string
        indices = {
            "Year": 4,     # "2017"
            "Month": 7,    # "2017:01"
            "Day": 10,     # "2017:01:15"
            "Hour": 13,    # "2017:01:15:23"
            "Minute": 16,  # "2017:01:15:23:59"
            "Second": 19   # "2017:01:15:23:59:59"
        }
        idx = indices[granularity]
        
        # Slice the start/end strings to the target granularity
        start_prefix = start[:idx]
        end_prefix = end[:idx]
        
        res = []
        for ts, log_id in self.logs:
            # Slice the log's timestamp to the same level and compare alphabetically!
            if start_prefix <= ts[:idx] <= end_prefix:
                res.append(log_id)
        return res
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
