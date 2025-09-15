#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k is still greater than 0, remove from the end
        stack = stack[:-k] if k else stack

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else '0'
        
# @lc code=end

