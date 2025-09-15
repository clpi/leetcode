#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                # Justify the current line
                for i in range(maxWidth - current_length):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
        
        # Handle the last line
        last_line = ' '.join(current_line).ljust(maxWidth)
        result.append(last_line)
        
        return result
        
# @lc code=end

