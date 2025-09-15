#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.

Time complexity: O(N) where N is # of nodes in linked list
Space complexity: O(N).
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
from typing import Optional
class Solution:

    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
        
# @lc code=end

