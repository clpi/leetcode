#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(max_sum):
            count, current_sum = 1, 0
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
                else:
                    current_sum += num
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
# @lc code=end

