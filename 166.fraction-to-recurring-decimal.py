#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(result)
        
        result.append(".")
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                break
            
            remainder_map[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator
        
        return ''.join(result)
        
# @lc code=end

