#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        num_seen = False
        dot_seen = False
        e_seen = False
        num_after_e = True

        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
                num_after_e = True
            elif char == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char in 'eE':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False
            elif char in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
            else:
                return False

        return num_seen and num_after_e
        
# @lc code=end

