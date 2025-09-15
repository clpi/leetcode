#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:

    def maxRotateFunction(self, nums: list[int]) -> int:
        repeat = False
        for i, n in enumerate(nums):
            if repeat:
                continue
            if nums[i + 1] == n:
                repeat = True
                continue
            return i
        return -1
        
# @lc code=end

