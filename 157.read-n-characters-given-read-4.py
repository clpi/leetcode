#
# @lc app=leetcode id=157 lang=python3
#
# [157] Read N Characters Given Read4
#

# @lc code=start
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
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

