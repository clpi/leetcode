#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# Time complexity: O(k^2) where k is the row number.
#     - We iterate through the rows from 0 to r, and for each row,
#       we create a new list of size i+1, where i is the current row
#       number. The inner loop runs for i-1 iterations, which is O(k).
# Space complexity: O(k) for storing the current row of Pascal's Triangle.  
#     - The previous row is reused, so we do not need additional space
#       for storing all rows.  
# Space: O(k) + O(k) ~= O(k)

# @lc code=start
class Solution:

    def getRow(self, r: int) -> list[int]:
        prev = [1]
        for i in range(1, r + 1):
            curr = [1] * (i + 1)
            for j in range(1, i):
                curr[j] = prev[j - 1] + prev[j]
            prev = curr
        return prev
        
# @lc code=end

