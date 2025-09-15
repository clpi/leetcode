#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            result = max(result, h * (right - left))
            while left < right and height[left] <= h:
                left += 1
            while left < right and height[right] <= h:
                right -= 1
        return result
        
# @lc code=end

