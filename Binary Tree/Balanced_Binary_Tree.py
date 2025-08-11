"""
LeetCode #110: Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree
Date: 08-11-2025
Approach: 
    - Initially, I used recursion to track the left and the right node of the root separately.
    - After I found it was not efficient, I implemented a single traversal that calculates the height of each subtree.
Time: O(n), Space: O(h) # where h is the height of the tree
Notes: 
    - In balanced binary trees, the height of the two subtrees of any node never differs by more than one.
Read Solution: Yes for cleaning up the code and improving efficiency.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            
            leftH = check(node.left)
            if leftH == -1:
                return -1
            
            rightH = check(node.right)
            if rightH == -1:
                return -1

            if abs(leftH - rightH) > 1:
                return -1

            return max(leftH, rightH) + 1

        return check(root) != -1