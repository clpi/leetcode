#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], parent_val: int, length: int) -> int:
            if not node:
                return length
            
            if node.val == parent_val + 1:
                length += 1
            else:
                length = 1
            
            left_length = dfs(node.left, node.val, length)
            right_length = dfs(node.right, node.val, length)
            
            return max(length, left_length, right_length)

        return dfs(root, float('-inf'), 0)
        
# @lc code=end

