"""
LeetCode #54: Spiral Matrix  
Link: https://leetcode.com/problems/spiral-matrix/  
Date: 07-15-2025  
Approach:  
    - Followed the pseudocode from LeetCode AI to understand the spiral traversal logic.  
    - Used four boundary pointers (top, bottom, left, right) to control the direction of traversal.  
    - Traversed in the order: → ↓ ← ↑, updating the boundaries after each pass.
Time: O(m * n), where m = rows and n = columns  
Space: O(1) extra space (excluding the output list)
Notes:  
    - Learned to carefully update boundary conditions to avoid duplicates or index errors.  
    - The order of traversal must match the direction of boundary updates.  
    - Using `range(left, right + 1)` and similar adjustments ensures full coverage of each row/column.  
    - Good practice for 2D matrix traversal and pointer control.
Read Solution: Yes (used LeetCode AI pseudocode)
"""


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right):
                res.append(matrix[top][i])

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            top += 1
            right -= 1

            if top > bottom or left > right:
                return res

            for i in range(right, left, -1):
                res.append(matrix[bottom][i])

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            bottom -= 1
            left += 1

            print(res)

        return res