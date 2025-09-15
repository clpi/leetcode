#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(prev + num, curr)
            return curr
        
        # Rob either from the first house to the second last or from the second house to the last
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        
# @lc code=end

