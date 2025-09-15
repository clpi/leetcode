#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
# Iterative BFS
from collections import deque
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1: return False
        adjlist = [[] for _ in range(n)]
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
        visited = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in adjlist[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return len(visited) == n
        
# @lc code=end

