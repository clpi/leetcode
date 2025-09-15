#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#

# @lc code=start
class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        
        # Initialize the first row
        for j in range(k):
            costs[0][j] = costs[0][j]
        
        for i in range(1, n):
            for j in range(k):
                # Find the minimum cost of painting the previous house with a different color
                min_cost = int(1e9)
                for m in range(k):
                    if m != j:
                        min_cost = min(min_cost, costs[i-1][m])
                costs[i][j] += min_cost
        
        return min(costs[-1])
        
# @lc code=end

