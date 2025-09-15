#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(N), N = number of nodes

class Solution:

    def isPalindrome(self, head: ListNode | None) -> bool:
        arr, curr = [], head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr == arr[::-1]
        
# @lc code=end

