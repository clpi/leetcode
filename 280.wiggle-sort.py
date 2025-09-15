#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n - 1) // 2
        left, right = mid, n - 1

        result = []
        for i in range(n):
            if i % 2 == 0:
                result.append(nums[left])
                left -= 1
            else:
                result.append(nums[right])
                right -= 1

        for i in range(n):
            nums[i] = result[i]
        
# @lc code=end

