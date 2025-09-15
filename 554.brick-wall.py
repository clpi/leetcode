#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        from collections import defaultdict
        
        edge_count = defaultdict(int)
        
        for row in wall:
            edge_position = 0
            for brick in row[:-1]:  # Exclude the last brick to avoid counting the wall's edge
                edge_position += brick
                edge_count[edge_position] += 1

        # The least number of bricks crossed is the total number of rows minus the maximum count of edges
        return len(wall) - max(edge_count.values(), default=0)

# @lc code=end

