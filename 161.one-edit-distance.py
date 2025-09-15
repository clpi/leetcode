#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#

# @lc code=start
class Solution:

    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)

        if abs(len_s - len_t) > 1:
            return False

        if len_s < len_t:
            s, t = t, s
            len_s, len_t = len_t, len_s

        found_difference = False
        i, j = 0, 0

        while i < len_s and j < len_t:
            if s[i] != t[j]:
                if found_difference:
                    return False
                found_difference = True

                if len_s == len_t:
                    j += 1
            else:
                j += 1
            i += 1
        return True if found_difference or len_s > len_t else False

# @lc code=end

