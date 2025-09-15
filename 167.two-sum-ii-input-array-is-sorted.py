#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start

# Time complexity: O(N), the input array is traversed once.
# Space complexity: O(1), we only use additional space to store two 
#     indices and the sum, so complexity is constant.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            curr_sum = numbers[low] + numbers[high]
            if curr_sum == target:
                return [low + 1, high + 1]
            elif curr_sum < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
        
# @lc code=end

