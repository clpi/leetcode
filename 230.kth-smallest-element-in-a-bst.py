#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            count += 1
            
            if count == k:
                return current.val
            
            current = current.right
        
        return -1
        
# @lc code=end

