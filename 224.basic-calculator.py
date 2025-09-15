#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operation = '+'
        s = s.replace(' ', '')

        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if char in '+-()' or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '(':
                    stack.append('(')
                current_number = 0
                operation = char

            if char == ')':
                temp_sum = 0
                while stack and stack[-1] != '(':
                    temp_sum += stack.pop()
                stack.pop()
                stack.append(temp_sum)
        return sum(stack) + current_number if operation == '+' else sum(stack) - current_number

# @lc code=end

