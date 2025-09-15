#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode|None) -> list[list[int]]:
        if not root:
            return []

        from collections import defaultdict, deque

        column_table = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            column_table[column].append(node.val)

            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))

        # Extract the columns and sort them
        min_column = min(column_table.keys())
        max_column = max(column_table.keys())
        return [column_table[col] for col in range(min_column, max_column + 1)]
