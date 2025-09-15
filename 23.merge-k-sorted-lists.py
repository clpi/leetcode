#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start

# Brute force:
# - Traverse all lists, collect all values of nodes into an array
# - Sort and iterate over this array to get proper value of nodes
# - Create a new sorted linked list and extend it with the sorted nodes

# Time complexity: O(n log n) where n is the total number of nodes
#   - O(n) to collect all values from the lists
#   - O(n log n) to sort the values
#   - O(n) to iterate over the sorted values and create new list
# Space complexity: O(n) where n is the total number of nodes
#   - O(n) to sort (depends on sorting algorithm space)
#   - O(n) cost to create new linked list

from typing import Optional, List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, 
                    lists: list[ListNode | None]
                    ) -> ListNode | None:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

        
# @lc code=end

