#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#

# @lc code=start

# Time complexity: O(N), it's two passes over the string.
# Space complexity: O(1), since it's a constant space solution

class Solution:
    def reverse(self, l: list[str], left: int, right: int):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverseWord(self, l: list[str]) -> None:
        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != ' ':
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1


    def reverseWords(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Reverse the entire string
        self.reverse(s, 0, len(s) - 1)
        # Reverse each word in the reversed string
        self.reverseWord(s)

        
# @lc code=end

