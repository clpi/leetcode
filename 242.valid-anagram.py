#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# Time complexity: O(N log N)
#    - Comparing two strings costs O(N)
#    - Sorting (time sort) dominates overall time complexity, O(N log N)
# Space complexity: O(1)
#    - Space depends on sorting implementation
#    - Usually costs O(1) auxiliary space if heapsort is used

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        
# @lc code=end

