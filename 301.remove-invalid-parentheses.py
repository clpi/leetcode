#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def backtrack(start: int, left_count: int, right_count: int, current: str):
            if left_count < 0 or right_count < 0 or left_count > right_count:
                return
            
            if start == len(s):
                if left_count == 0 and right_count == 0 and is_valid(current):
                    results.add(current)
                return
            
            char = s[start]
            if char == '(':
                backtrack(start + 1, left_count - 1, right_count, current + char)
                backtrack(start + 1, left_count, right_count, current)
            elif char == ')':
                backtrack(start + 1, left_count, right_count - 1, current + char)
                backtrack(start + 1, left_count, right_count, current)
            else:
                backtrack(start + 1, left_count, right_count, current + char)

        results = set()
        left_to_remove = s.count('(') - s.count(')')
        right_to_remove = s.count(')') - s.count('(')
        backtrack(0, left_to_remove, right_to_remove, "")
        
        return list(results)
        
# @lc code=end

