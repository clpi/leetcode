#
# @lc app=leetcode id=439 lang=python3
#
# [439] Ternary Expression Parser
#

# @lc code=start
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        i = len(expression) - 1

        while i >= 0:
            if expression[i] == '?':
                true_expr = stack.pop()
                false_expr = stack.pop()
                condition = stack.pop()
                if condition == 'T':
                    stack.append(true_expr)
                else:
                    stack.append(false_expr)
            else:
                stack.append(expression[i])
            i -= 1

        return stack[0]
        
# @lc code=end

