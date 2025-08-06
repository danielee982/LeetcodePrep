"""
LeetCode #876: Middle of the Linked List
Link: https://leetcode.com/problems/middle-of-the-linked-list
Date: 08-06-2025
Approach: 
    - Use the slow/fast pointer technique to find the middle of the linked list
    - Move the fast pointer two steps for every one step of the slow pointer
Time: O(n), Space: O(1)
Notes: 
    - If the list is empty, the middle is None
    - If the list has an even number of elements, the second middle element is returned
Read Solution: No
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow