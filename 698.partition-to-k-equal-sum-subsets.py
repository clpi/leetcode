#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target_sum = total_sum // k
        nums.sort(reverse=True)
        
        if nums[0] > target_sum:
            return False
        
        subsets = [0] * k
        
        def backtrack(index: int) -> bool:
            if index == len(nums):
                return all(subset == target_sum for subset in subsets)
            
            for i in range(k):
                if subsets[i] + nums[index] <= target_sum:
                    subsets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    subsets[i] -= nums[index]
                
                if subsets[i] == 0:
                    break
            return False
        
        # Initialize subsets to zero
        subsets = [0] * k

        # Start backtracking from the first index
        return backtrack(0)

# @lc code=end

