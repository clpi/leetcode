#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        n = len(nums)
        total_distance = 0
        
        for i in range(32):
            count_one = sum((num >> i) & 1 for num in nums)
            count_zero = n - count_one
            total_distance += count_one * count_zero

        return total_distance

