#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, path):
            if path not in result:
                result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        nums.sort()
        result = []
        backtrack(0, [])
        return result
        
# @lc code=end

