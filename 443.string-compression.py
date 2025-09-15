#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0
        read_index = 0
        n = len(chars)

        while read_index < n:
            current_char = chars[read_index]
            count = 0

            while read_index < n and chars[read_index] == current_char:
                read_index += 1
                count += 1

            chars[write_index] = current_char
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index
        
# @lc code=end

