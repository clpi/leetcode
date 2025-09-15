#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        sign, res, idx, n = 1, 0, 0, len(s)
        i_max, i_min = pow(2, 31) - 1, -pow(2, 31)
        while idx < n and s[idx] == " ":
            idx += 1
        if idx < n and s[idx] == "+":
            sign = 1
            idx += 1
        elif idx < n and s[idx] == "-":
            sign = -1
            idx += 1
        while idx < n and s[idx].isdigit():
            num = int(s[idx])
            if (res > i_max // 10) or \
               (res == i_max // 10 and num > i_max % 10):
                return i_max if sign == 1 else i_min
            res = 10 * res + num
            idx += 1
        return sign * res

# @lc code=end

