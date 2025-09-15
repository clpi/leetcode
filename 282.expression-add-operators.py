#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []
        def backtrack(index: int, path: str, value: int, prev_operand: int):
            if index == len(num) and value == target:
                result.append(path)
                return
            
            for i in range(index, len(num)):
                current_str = num[index:i + 1]
                current_num = int(current_str)
                
                if index == 0:
                    # First number, no operator needed
                    backtrack(i + 1, current_str, current_num, current_num)
                else:
                    # Addition
                    backtrack(i + 1, path + '+' + current_str, value + current_num, current_num)
                    # Subtraction
                    backtrack(i + 1, path + '-' + current_str, value - current_num, -current_num)
                    # Multiplication
                    backtrack(i + 1, path + '*' + current_str,
                              value - prev_operand + prev_operand * current_num,
                              prev_operand * current_num)

        backtrack(0, '', 0, 0)
        return result
        
# @lc code=end

