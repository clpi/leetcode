#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start

# Time complexity: O(N + M), where N & M are lengths of a and b
# Space complexity: O(max(N, M)) to store the answer

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
        
# @lc code=end

