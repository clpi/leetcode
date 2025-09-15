#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(node: Optional[TreeNode], values: List[int]):
            if not node:
                return
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)

        values = []
        inorder(root, values)

        # Find the closest k values to the target
        left, right = 0, len(values) - 1
        while right - left >= k:
            if abs(values[left] - target) < abs(values[right] - target):
                right -= 1
            else:
                left += 1

        return values[left:left + k]
        
# @lc code=end

