#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        
        current = root
        next_level_start = None
        prev = None
        
        while current:
            if current.left:
                if prev:
                    prev.next = current.left
                else:
                    next_level_start = current.left
                prev = current.left
            
            if current.right:
                if prev:
                    prev.next = current.right
                else:
                    next_level_start = current.right
                prev = current.right
            
            current = current.next
        
        self.connect(next_level_start)
        return root
        
# @lc code=end

