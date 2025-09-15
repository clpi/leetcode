#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        prefix_sum = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            if k != 0:
                current_sum %= k
            
            if current_sum in prefix_sum:
                if i - prefix_sum[current_sum] > 1:
                    return True
            else:
                prefix_sum[current_sum] = i
        
        return False
        
# @lc code=end

