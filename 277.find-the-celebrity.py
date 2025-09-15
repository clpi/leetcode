#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find the Celebrity
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        
        # Find a candidate for celebrity
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        # Verify the candidate
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1
        
        return candidate
        
# @lc code=end

