#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping_s_to_t = {}
        mapping_t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s_to_t:
                mapping_s_to_t[char_s] = char_t
            if char_t not in mapping_t_to_s:
                mapping_t_to_s[char_t] = char_s

            if mapping_s_to_t[char_s] != char_t or mapping_t_to_s[char_t] != char_s:
                return False

        return True
        
# @lc code=end

