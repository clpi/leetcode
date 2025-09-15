#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#

# @lc code=start
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0
        self.diag2 = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at (row, col).
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            mark = 1
        else:
            mark = -1
        
        self.rows[row] += mark
        self.cols[col] += mark
        
        if row == col:
            self.diag1 += mark
        if row + col == self.n - 1:
            self.diag2 += mark
        
        if (abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.diag1) == self.n or 
            abs(self.diag2) == self.n):
            return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# @lc code=end

