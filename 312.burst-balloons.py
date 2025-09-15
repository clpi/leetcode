#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Add 1s to the beginning and end of the list
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] will store the maximum coins that can be obtained by bursting balloons from i to j
        dp = [[0] * n for _ in range(n)]
        
        # Iterate over the length of the subarray
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                # Calculate the maximum coins for this subarray
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], 
                                          dp[left][k] + dp[k][right] + nums[left] * nums[k] * nums[right])
        
        return dp[0][n - 1]
        
# @lc code=end

