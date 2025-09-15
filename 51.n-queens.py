#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int, cols: set, diagonals1: set, diagonals2: set, board: List[str]):
            if row == n:
                result.append(board[:])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                board[row] = '.' * col + 'Q' + '.' * (n - col - 1)
                
                backtrack(row + 1, cols, diagonals1, diagonals2, board)
                
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        result = []
        board = ['.' * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result
        
# @lc code=end

