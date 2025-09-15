#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return s == s[::-1]

        if not s:
            return ""

        # Find the longest palindromic prefix
        for i in range(len(s), -1, -1):
            if is_palindrome(s[:i]):
                break

        # The rest of the string needs to be added in reverse order
        suffix = s[i:][::-1]
        return suffix + s
        
# @lc code=end

