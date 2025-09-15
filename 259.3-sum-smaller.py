#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

# @lc code=start
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1

        return count
        
# @lc code=end

