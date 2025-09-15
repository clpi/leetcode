#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
# Time complexity: O(n + m): performing n + 2m reads, n + 2m writes. Constants ignored in big O
# Space complexity: O(1), unlike other approach, no array needed
class Solution:
    def merge(self, n1: list[int], m: int, n2: list[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            elif p1 >= 0 and n1[p1] > n2[p2]:
                n1[p] = n1[p1]
                p1 -= 1
            else:
                n1[p] = n2[p2]
                p2 -= 1
        
# @lc code=end

