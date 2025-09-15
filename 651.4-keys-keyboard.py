#
# @lc app=leetcode id=651 lang=python3
#
# [651] 4 Keys Keyboard
#

# @lc code=start
class Solution:
    def maxA(self, n: int) -> int:
        """Calculate the maximum number of 'A's that can be produced with n keystrokes.
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0 
        # If n is 1 to 6, the maximum is simply n  
        # because we can only press 'A' or 'Ctrl+A', 'Ctrl+C', 'Ctrl+V' once.
        # For n > 6, we can use dynamic programming to find the maximum.   
        if n <= 6:
            return n   
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            for j in range(3, i - 2):
                dp[i] = max(dp[i], dp[i - j] * (j + 1))
        return dp[n]    
        
# @lc code=end

