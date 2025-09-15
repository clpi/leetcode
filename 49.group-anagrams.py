#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
import collections

# Time complexity: O(NKlogK) where:
#   K is the maximum length of a string in the input list `strs`.
#   N is the number of strings and K is the maximum length of a string.
#   - Each string is sorted in O(KlogK) time.
#   - The overall complexity is O(NKlogK).
# Space complexity: O(NK), the total information stored in the result.

class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())
        
# @lc code=end

