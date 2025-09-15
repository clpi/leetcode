#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# Time complexity: O(N*2^N) to generate all subsets, then copy them into the output list
# Space complexity: O(N) for the current subset and O(2^N) for the output list

# @lc code=start
class Solution:

    def __init__(self):
        self.output = []

    def backtrack(self, first: int, curr: list[int], nums: list[int]):
        self.output.append(curr[:])
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.output
        
# @lc code=end

