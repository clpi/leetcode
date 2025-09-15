#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        if target == 0 or target == x or target == y or target == x + y:
            return True
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        return target % gcd(x, y) == 0
        
# @lc code=end

