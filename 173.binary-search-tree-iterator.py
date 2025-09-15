#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode|None):
        self.stack = []
        self._push_left(root)

    def next(self) -> int:
        if not self.hasNext():
            return -1
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def _push_left(self, node: TreeNode|None):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

