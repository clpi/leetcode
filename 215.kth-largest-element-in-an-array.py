#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

# Time complexity: O(n log n), sorting nums requires O(n log n) time.
# Space complexity: O(log n) or O(n):
#     - In Python, the sort() method uses Timesort, which has worst case space complexity of O(n)

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]
        
# @lc code=end

