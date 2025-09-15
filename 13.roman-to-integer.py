#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = i = 0
        while i < len(s):
            n, v = len(s), s[i:i + 2]
            if i < n - 1 and v in map:
                total += map[v]
                i += 1
            else:
                total += map[s[i]]
            i += 1
        return total


        
# @lc code=end

