#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#

# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block_comment = False
        current_line = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if line[i:i+2] == '*/':
                        in_block_comment = False
                        i += 2
                    else:
                        i += 1
                else:
                    if line[i:i+2] == '/*':
                        in_block_comment = True
                        i += 2
                    elif line[i:i+2] == '//':
                        break
                    else:
                        current_line.append(line[i])
                        i += 1

            if not in_block_comment and current_line:
                result.append(''.join(current_line))
                current_line = []

        return result

# @lc code=end

