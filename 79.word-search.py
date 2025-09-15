#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or board[r][c] != word[index]:
                return False
            
            visited[r][c] = True
            found = (dfs(r + 1, c, index + 1) or 
                     dfs(r - 1, c, index + 1) or 
                     dfs(r, c + 1, index + 1) or 
                     dfs(r, c - 1, index + 1))
            visited[r][c] = False
            
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
        
# @lc code=end

