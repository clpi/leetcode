#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '*' else 9

        for i in range(2, n + 1):
            if s[i - 1] == '*':
                dp[i] += dp[i - 1] * 9
            elif s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if s[i - 2] == '*':
                if s[i - 1] == '*':
                    dp[i] += dp[i - 2] * 15
                elif '0' <= s[i - 1] <= '6':
                    dp[i] += dp[i - 2] * 2
                else:
                    dp[i] += dp[i - 2]
            elif '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

            dp[i] %= MOD

        return dp[n]
        
# @lc code=end

