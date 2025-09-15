#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
import random
class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        indices = [i for i, num in enumerate(self.nums) if num == target]
        return random.choice(indices) if indices else -1
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

