"""
LeetCode #235: Lowest Common Ancestor of a Binary Search Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
Date: 08-13-2025
Approach: 
    - Use the properties of the BST to find the LCA.
Time: O(h), Space: O(1)
Notes: 
    - The LCA is the deepest node that is an ancestor to both p and q.
Difficulty: Medium
Read Solution: No
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root
        

        while temp:
            if p.val < temp.val and q.val < temp.val:
                temp = temp.left
            elif p.val > temp.val and q.val > temp.val:
                temp = temp.right
            else:
                return temp