#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height))
            events.append((right, height))

        events.sort()
        result = []
        live_heights = [0]
        for x, h in events:
            if h < 0:
                live_heights.append(-h)
            else:
                live_heights.remove(h)
            current_max = max(live_heights)
            if not result or result[-1][1] != current_max:
                result.append((x, current_max))
        return result

# @lc code=end

