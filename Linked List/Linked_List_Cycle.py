"""
LeetCode #141: Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle
Date: 08-04-2025
Approach: 
    - I used a set to keep track of visited nodes by pushing each node into the set as I traverse the linked list.
    - If I encounter a node that is already in the set, it means there is a cycle.
Time: O(n), Space: O(n)
Notes: 
    - I learned that a set is based on a hash table, which allows for O(1) average time complexity for lookups.
    - It can also be solved using two pointers, which is more space-efficient.
      One pointer moves one step at a time, while the other moves two steps at a time.
Read Solution: No
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        my_set = set()

        while head:
            if head in my_set:
                return True
            
            my_set.add(head)
            head = head.next
        
        return False