#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        if not prices:
            return 0

        n = len(prices)
        hold = -prices[0] - fee
        cash = 0

        for i in range(1, n):
            hold = max(hold, cash - prices[i] - fee)
            cash = max(cash, hold + prices[i])

        return cash
        
# @lc code=end

