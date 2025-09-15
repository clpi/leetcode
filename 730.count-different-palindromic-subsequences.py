#
# @lc app=leetcode id=730 lang=python3
#
# [730] Count Different Palindromic Subsequences
#

# @lc code=start
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    low, high = i + 1, j - 1
                    while low <= high and s[low] != s[i]:
                        low += 1
                    while low <= high and s[high] != s[j]:
                        high -= 1

                    if low > high:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    elif low == high:
                        dp[i][j] = dp[i + 1][j - 1] + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + dp[i][low - 1] + dp[high + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

        return dp[0][n - 1]
        
# @lc code=end

