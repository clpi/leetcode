#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:

    # Time complexity: O(N), N = num of elements in the num array.
        # We traverse the array twice:
            # Once to construct the array of `result`
            # Once to update the array of `result` with the product of elements
    # Space complexity: O(1) since the problem statement says that the output
        # array does not count towards the space complexity.

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        for i in range(1, n):
            result[i] = nums[i - 1] * result[i - 1]
        # R contains the product of all the elements to the right
        # The rightmost element at index `length - 1`
        r = 1
        for i in reversed(range(n)):
            result[i] *= r
            r *= nums[i]
        return result


        
# @lc code=end

