#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: list[list[int]], 
               newInterval: list[int]) -> list[list[int]]:
        merged = []
        i = 0
        n = len(intervals)
        # Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1 
        merged.append(newInterval)
        # Add all remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1
        return merged
        
# @lc code=end

