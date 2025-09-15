#
# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#

# @lc code=start
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if n == 0:
            return 0
        if presses == 0:
            return 1
        if presses == 1:
            return min(4, n)
        if presses == 2:
            if n == 1:
                return 2
            elif n == 2:
                return 3
            else:
                return min(8, n)
        return min(8, n)
        
# @lc code=end

