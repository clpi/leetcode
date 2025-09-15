#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode|None, k: int) -> Optional[ListNode]:
        def reverseLinkedList(head: ListNode, k: int) -> ListNode:
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev

        count = 0
        current = head
        
        # Count the number of nodes in the linked list
        while current:
            count += 1
            current = current.next
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        # Reverse nodes in k-group
        while count >= k:
            group_start = group_prev.next
            group_end = group_start
            
            for _ in range(k - 1):
                group_end = group_end.next
            
            next_group_start = group_end.next
            
            # Reverse the k-group
            group_end.next = None
            group_prev.next = reverseLinkedList(group_start, k)
            group_start.next = next_group_start
            
            # Move the group_prev pointer forward
            group_prev = group_start
            
            count -= k
        
        return dummy.next
        
# @lc code=end

