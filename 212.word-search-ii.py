#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word
        result = set()
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c, node):
            if '#' in node:
                result.add(node['#'])
                del node['#']
            if not node:
                return
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc] in node:
                    dfs(nr, nc, node[board[nr][nc]])
            visited[r][c] = False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie[board[r][c]])
        return list(result) 
