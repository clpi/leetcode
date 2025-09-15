#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#

# @lc code=start
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same = k
        diff = k * (k - 1)
        
        for i in range(2, n):
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same, new_diff
        
        return same + diff
        
# @lc code=end

