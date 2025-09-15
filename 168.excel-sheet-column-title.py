#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            ch = chr(columnNumber % 26 + ord('A'))
            result.append(ch)
            columnNumber //= 26
        result.reverse()
        return ''.join(result)

# @lc code=end

