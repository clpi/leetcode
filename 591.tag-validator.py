#
# @lc app=leetcode id=591 lang=python3
#
# [591] Tag Validator
#

# @lc code=start
class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        n = len(code)

        while i < n:
            if code[i] == '<':
                if i + 1 < n and code[i + 1] == '/':
                    # Closing tag
                    j = code.find('>', i)
                    if j == -1 or not stack or stack[-1] != code[i + 2:j]:
                        return False
                    stack.pop()
                    i = j + 1
                else:
                    # Opening tag
                    j = code.find('>', i)
                    if j == -1 or j == i + 1 or j - i > 10:
                        return False
                    tag = code[i + 1:j]
                    if not tag.isalpha() or not tag.islower():
                        return False
                    stack.append(tag)
                    i = j + 1
            elif code[i] == '&':
                # Character reference
                j = code.find(';', i)
                if j == -1 or j == i + 1:
                    return False
                i = j + 1
            else:
                return False

        return not stack and (n >= 7 and code.startswith('<') and code.endswith('>'))
        
# @lc code=end

