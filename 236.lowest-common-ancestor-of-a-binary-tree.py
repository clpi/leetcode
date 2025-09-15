#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time complexity: O(N), where N is the number of nodes in the binary tree.
    # Worst case, we traverse all nodes once.
# Space complexity: O(N).
    # Worst case, the recursion stack utilizes O(N) space, since the height
    # of a skewed binary tree can be N.

class Solution:

    def __init__(self):
        self.lca: TreeNode | None = None

    def lowestCommonAncestor(self, 
                             root: TreeNode, 
                             p: TreeNode, 
                             q: TreeNode
                             ) -> TreeNode:
        def dfs(curr: TreeNode) -> bool:
            if not curr:
                return False
            # Traverse, return bool for l, r, mid
            l, r = dfs(curr.left), dfs(curr.right)
            mid = curr == p or curr == q
            # If any two of the three flags are True:
            if mid + l + r >= 2:
                self.lca = curr
            # Return True if either of the three bool values is True
            return mid or l or r
        # Traverse (dfs) the tree
        dfs(root)
        return self.lca
        


        
        
# @lc code=end

