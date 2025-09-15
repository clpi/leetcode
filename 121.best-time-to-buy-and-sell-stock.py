#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# Time complexity: O(n). Only a single pass is needed to find minimum
# Space complexity: O(1). Only two variables are used.

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pmin, pmax = float('inf'), 0
        for price in prices:
            if price < pmin:
                pmin = price
            elif price - pmin > pmax:
                pmax = price - pmin
        return pmax
# @lc code=end

