#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def search_from_center(s: str, l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return r - l - 1
        
        start, end = 0, 0
        for i in range(len(s)):
            odd = search_from_center(s, i, i)
            even = search_from_center(s, i, i + 1)
            len_max = max(odd, even)
            if len_max > end - start:
                start = i - (len_max - 1) // 2
                end = i + len_max // 2
        return s[start:end + 1]

        
# @lc code=end

