#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index
        
# @lc code=end

