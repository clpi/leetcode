#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand_around_center(left: int, right: int):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # Odd length palindromes
            expand_around_center(i, i)
            # Even length palindromes
            expand_around_center(i, i + 1)

        return count
        
# @lc code=end

