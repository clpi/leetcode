#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#

# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> List[int]:
        n = len(nums)
        if n < 3 * k:
            return []

        # Calculate prefix sums
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Calculate max sum for each subarray of length k
        max_sum = [0] * (n - k + 1)
        for i in range(n - k + 1):
            max_sum[i] = prefix_sum[i + k] - prefix_sum[i]

        # Calculate left max sums
        left_max = [0] * (n - k + 1)
        left_index = 0
        for i in range(n - k + 1):
            if max_sum[i] > max_sum[left_index]:
                left_index = i
            left_max[i] = left_index

        # Calculate right max sums
        right_max = [0] * (n - k + 1)
        right_index = n - k
        for i in range(n - k, -1, -1):
            if max_sum[i] >= max_sum[right_index]:
                right_index = i
            right_max[i] = right_index

        # Find the maximum sum of three non-overlapping subarrays
        max_total = 0
        result_indices = [-1, -1, -1]
        
        for j in range(k, n - 2 * k + 1):
            i = left_max[j - k]
            l = right_max[j + k]
            total = max_sum[i] + max_sum[j] + max_sum[l]
            
            if total > max_total:
                max_total = total
                result_indices = [i, j, l]

        return result_indices
        
# @lc code=end

