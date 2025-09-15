#
# @lc app=leetcode id=308 lang=python3
#
# [308] Range Sum Query 2D - Mutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.prefix_sum[i][j] = (matrix[i - 1][j - 1] +
                                         self.prefix_sum[i - 1][j] +
                                         self.prefix_sum[i][j - 1] -
                                         self.prefix_sum[i - 1][j - 1])
        

    def update(self, row: int, col: int, val: int) -> None:
        old_value = self.matrix[row][col]
        self.matrix[row][col] = val

        for i in range(row + 1, self.rows + 1):
            for j in range(col + 1, self.cols + 1):
                self.prefix_sum[i][j] += (val - old_value)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix_sum[row2 + 1][col2 + 1] -
                self.prefix_sum[row1][col2 + 1] -
                self.prefix_sum[row2 + 1][col1] +
                self.prefix_sum[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

