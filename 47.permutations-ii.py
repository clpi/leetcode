#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])
                return
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]  # backtrack
        result = []
        backtrack()
        return result
        
# @lc code=end

