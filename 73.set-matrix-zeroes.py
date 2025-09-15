#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# Time complexity: O(MN) where M: num of rows, N: num of columns
# Space complexity: O(1) since we modify the matrix in-place

# @lc code=start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col, r, c = False, len(matrix), len(matrix[0])
        for i in range(r):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, r):
            for j in range(1, c):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0
        if is_col:
            for i in range(r):
                matrix[i][0] = 0
        
# @lc code=end

