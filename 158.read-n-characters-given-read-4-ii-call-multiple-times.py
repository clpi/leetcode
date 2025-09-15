#
# @lc app=leetcode id=158 lang=python3
#
# [158] Read N Characters Given read4 II - Call Multiple Times
#

# @lc code=start
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def read(self, buf: list[str], n: int) -> int:
        buf4 = [''] * 4
        total_chars_read = 0
        
        while total_chars_read < n:
            chars_read = read4(buf4)
            if chars_read == 0:
                break
            
            for i in range(min(chars_read, n - total_chars_read)):
                buf[total_chars_read + i] = buf4[i]
            
            total_chars_read += chars_read
            if chars_read < 4:
                break
        
        return total_chars_read
        
# @lc code=end

