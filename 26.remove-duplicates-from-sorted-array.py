#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# Time complexity: O(N), two pointers, both pointers traverse array at most once
# Space complexity: O(1) since we dont use any extra space
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        return idx
        
# @lc code=end

