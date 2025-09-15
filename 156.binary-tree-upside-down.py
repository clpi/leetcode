#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode|None) -> TreeNode|None:
        if not root or (not root.left and not root.right):
            return root

        new_root = self.upsideDownBinaryTree(root.left)

        if root.left:
            root.left.left = root.right
            root.left.right = root
            root.left = None
            root.right = None

        return new_root
        
# @lc code=end

