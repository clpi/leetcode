#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root or not p:
            return None
        
        successor = None
        
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                break
        
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        return successor
        
# @lc code=end

