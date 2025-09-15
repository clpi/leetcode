#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import Counter

# Time complexity: O(N)
#   We traverse string of length N two times
#   Space complexity: O(1) constant because alphabet size is fixed

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i     
        return -1
        
# @lc code=end

