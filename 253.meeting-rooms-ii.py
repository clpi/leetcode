#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        used, n = 0, len(intervals)
        start, end = sorted([i[0] for i in intervals]), sorted(i[1] for i in intervals)
        startp, endp = 0, 0
        while startp < n:
            if start[startp] >= end[endp]:
                used -= 1
                endp += 1
            used += 1
            startp += 1
        return used
        
# @lc code=end

