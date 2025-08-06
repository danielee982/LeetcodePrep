"""
LeetCode #206: Reversed Linked List
Link: https://leetcode.com/problems/reverse-linked-list
Date: 08-06-2025
Approach:
    - Use recursion to reverse the linked list
    - Change the next pointer of each node to point to the previous node
Time: O(n), Space: O(n)
Notes:
    - The base case for the recursion is when the head is None or head.next is None
    - The recursive call will reverse the rest of the list and return the new head
Read Solution: No
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        temp = head
        res = self.reverseList(temp.next)
        temp.next.next = temp
        temp.next = None

        return res
    
"""
LeetCode #206: Reversed Linked List
Link: https://leetcode.com/problems/reverse-linked-list
Date: 08-06-2025
Approach:
    - Use iteraive approach to reverse the linked list
    - Change the next pointer of each node to point to the previous node
Time: O(n), Space: O(1)
Notes:
    - The iterative approach is more space-efficient than the recursive approach
Read Solution: Yes
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node