#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return float('inf')

        closest = root.val
        current = root

        while current:
            if abs(current.val - target) < abs(closest - target):
                closest = current.val
            
            if target < current.val:
                current = current.left
            elif target > current.val:
                current = current.right
            else:
                break

        return closest

# @lc code=end

