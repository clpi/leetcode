#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode|None) -> int:
        if not root or (not root.left and not root.right):
            return -1

        def dfs(node: TreeNode) -> set[int]:
            if not node:
                return set()
            values = {node.val}
            values.update(dfs(node.left))
            values.update(dfs(node.right))
            return values

        unique_values = dfs(root)
        unique_values.discard(root.val)

        if not unique_values:
            return -1

        return min(unique_values)

        
# @lc code=end

