#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start
class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> List[List[int]]:
        if not mat1 or not mat2 or not mat1[0] or not mat2[0]:
            return []

        rows, cols = len(mat1), len(mat2[0])
        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(len(mat1[0])):
                if mat1[i][j] != 0:
                    for k in range(len(mat2[0])):
                        result[i][k] += mat1[i][j] * mat2[j][k]

        return result
        
# @lc code=end

