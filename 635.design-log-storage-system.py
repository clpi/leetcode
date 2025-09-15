#
# @lc app=leetcode id=635 lang=python3
#
# [635] Design Log Storage System
#

# @lc code=start
class LogSystem:

    def __init__(self):
        self.logs = []
        self.time_format = {
            "Year": "YYYY",
            "Month": "YYYY-MM",
            "Day": "YYYY-MM-DD",
            "Hour": "YYYY-MM-DD HH",
            "Minute": "YYYY-MM-DD HH:MM",
            "Second": "YYYY-MM-DD HH:MM:SS"
        }
        
    
    # Store a log with an ID and timestamp
    # @param id: The ID of the log
    # @param timestamp: The timestamp of the log in the format "YYYY-MM-DD HH:MM:SS"
    # @return: None

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))
        self.logs.sort(key=lambda x: x[1])  # Keep logs sorted by timestamp


    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start_format = self.time_format[granularity]
        end_format = self.time_format[granularity]

        # Adjust start and end timestamps to match the granularity
        start_timestamp = start[:len(start_format)]
        end_timestamp = end[:len(end_format)]

        result = []
        for log_id, timestamp in self.logs:
            if start_timestamp <= timestamp[:len(start_format)] <= end_timestamp:
                result.append(log_id)

        return result
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
# @lc code=end

