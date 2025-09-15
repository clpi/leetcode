#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        return odd_count <= 1
        
# @lc code=end

