#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive approach (O(nlogn) time complexity, O(n) space complexity)
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        paths = []
        def make_paths(root: TreeNode | None = root, path: str = "") -> list[str]:
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    make_paths(root.left, path)
                    make_paths(root.right, path)
        make_paths(root, "")
        return paths
            
    # Iterative approach (O(n) time complexity, O(n) space complexity)
    # def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
    #     if not root:
    #         return []
    #     paths, stack = [], [(root, str(root.val))]
    #     while stack:
    #         node, path = stack.pop()
    #         if not node.left and not node.right:
    #             paths.append(path)
    #         if node.left:
    #             stack.append((node.left, path + "->" + str(node.left.val)))
    #         if node.right:
    #             stack.append((node.right, path + "->" + str(node.right.val)))
    #     return paths
                
        
# @lc code=end

