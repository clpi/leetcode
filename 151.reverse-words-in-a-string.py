#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # Strip leading/trailing spaces and split by spaces
        words = s.strip().split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words with a single space
        return ' '.join(reversed_words)
        
# @lc code=end

