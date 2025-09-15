#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or stones[0] != 0:
            return False
        
        n = len(stones)
        dp = {i: set() for i in range(n)}
        dp[0].add(0)

        for i in range(n):
            for k in dp[i]:
                for jump in (k - 1, k, k + 1):
                    if jump > 0 and i + jump < n and stones[i + jump] == stones[i] + jump:
                        dp[i + jump].add(jump)

        return bool(dp[n - 1])

# @lc code=end

