#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
        
# @lc code=end

