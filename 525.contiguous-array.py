#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = 0
        max_length = 0
        index_map = {0: -1}

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in index_map:
                max_length = max(max_length, i - index_map[count])
            else:
                index_map[count] = i

        return max_length

# @lc code=end

