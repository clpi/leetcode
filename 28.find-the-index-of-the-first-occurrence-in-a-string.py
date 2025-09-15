#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for start in range(m - n + 1):
            for i in range(n):
                if needle[i] != haystack[start + i]:
                    break
                elif i == n - 1:
                    return start
        return -1
        
# @lc code=end

