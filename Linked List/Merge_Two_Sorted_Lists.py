"""
LeetCode #21: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists
Date: 08-04-2025
Approach: 
    - Initially, I tried to push elements from list2 into list1, but it was inefficient.
    - Instead, I created a new linked list and iterated through both lists, comparing their values.
Time: O(n+m), Space: O(1)
Notes: 
    - Optional[ListNode] means that the variable can be either a ListNode or None.
    - "current.next = list1 or list2" assigns the remaining non-null list to current.next.
Read Solution: No
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val >= list2.val:
                current.next = list2
                list2 = list2.next
            elif list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            
            current = current.next
        
        current.next = list1 or list2
        
        return head.next
