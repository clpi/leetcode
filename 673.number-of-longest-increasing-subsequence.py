#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        lengths = [1] * n
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[i] < lengths[j] + 1:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]

        max_length = max(lengths)
        return sum(counts[i] for i in range(n) if lengths[i] == max_length)
        
# @lc code=end

