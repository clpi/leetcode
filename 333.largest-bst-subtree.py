#
# @lc app=leetcode id=333 lang=python3
#
# [333] Largest BST Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int, int, bool]:
            if not node:
                return 0, float('inf'), float('-inf'), True
            
            left_size, left_min, left_max, is_left_bst = dfs(node.left)
            right_size, right_min, right_max, is_right_bst = dfs(node.right)

            if is_left_bst and is_right_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                return size, min(left_min, node.val), max(right_max, node.val), True
            else:
                return max(left_size, right_size), 0, 0, False

        return dfs(root)[0]
        
# @lc code=end

