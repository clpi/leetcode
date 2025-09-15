#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, char in enumerate(columnTitle):
            result *= 26
            # convert to ord without calling ord()
            result += (ord(char) - 65 + 1)

        return result
        
# @lc code=end

