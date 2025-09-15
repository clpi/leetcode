#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start
class Solution:


    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        prefix_sum = {0: -1}
        current_sum = 0
        max_length = 0

        for i, num in enumerate(nums):
            current_sum += num
            if current_sum == k:
                max_length = i + 1
            if current_sum - k in prefix_sum:
                max_length = max(max_length, i - prefix_sum[current_sum - k])
            prefix_sum[current_sum] = i

        return max_length

