#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]] if lower <= upper else []

        result = []
        prev = lower - 1

        for num in nums:
            if num > prev + 1:
                result.append([prev + 1, num - 1])
            prev = num

        if prev < upper:
            result.append([prev + 1, upper])

        return result
        
# @lc code=end

