#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        total_sum = sum(nums)
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        subset_sum = (total_sum + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]
# @lc code=end

