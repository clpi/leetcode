#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        bottom_left_value = 0

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            nonlocal max_depth, bottom_left_value
            if not node:
                return
            if depth > max_depth:
                max_depth = depth
                bottom_left_value = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return bottom_left_value

# @lc code=end

