#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = self.mySqrt(x >> 2) << 1
        r = l + 1
        return l if r * r > x else r
        
# @lc code=end

