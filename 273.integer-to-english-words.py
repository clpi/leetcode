#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            switcher = {
                1: "One", 2: "Two", 3: "Three", 4: "Four",
                5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
            }
            return switcher.get(num, "")

        def two_less_20(num):
            switcher = {
                10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
                14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
            }
            return switcher.get(num, "")

        def ten(num):
            switcher = {
                2: "Twenty", 3: "Thirty", 4: "Forty",
                5: "Fifty", 6: "Sixty", 7: "Seventy",
                8: "Eighty", 9: "Ninety"
            }
            return switcher.get(num, "")

        def helper(num):
            if num == 0:
                return ""
            elif num < 10:
                return one(num) + " "
            elif num < 20:
                return two_less_20(num) + " "
            elif num < 100:
                return ten(num // 10) + (one(num % 10) + " ") if num % 10 != 0 else ten(num // 10) + " "
            else:
                return one(num // 100) + " Hundred " + helper(num % 100)

        thousands = ["", " Thousand ", " Million ", " Billion "] 
        result = ""
        for i in range(len(thousands)):
            if num % (1000 ** (i + 1)) != num:
                result = helper((num // (1000 ** i)) % 1000) + thousands[i] + result
        return result.strip()
        
# @lc code=end

