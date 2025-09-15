#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 1

        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[0] * cols for _ in range(rows)]

        dp[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])

        for i in range(rows - 2, -1, -1):
            dp[i][cols - 1] = max(1, dp[i + 1][cols - 1] - dungeon[i][cols - 1])

        for j in range(cols - 2, -1, -1):
            dp[rows - 1][j] = max(1, dp[rows - 1][j + 1] - dungeon[rows - 1][j])

        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])

        return dp[0][0]
        
# @lc code=end

