"""
LeetCode #226: Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree
Date: 08-11-2025
Approach: 
    - User recursion to swap the left and right children of each node.
Time: O(n), Space: O(h) # where h is the height of the tree
Notes: 
    - I can try with an iterative approach using a queue or stack.
Read Solution: No
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        temp = left
        root.left = right
        root.right = temp

        return root
