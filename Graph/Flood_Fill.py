"""
LeetCode #733: Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Date: 08-13-2025
Approach: 
    - Use DFS to recolor all connected pixels with the same original color as image[sr][sc].
    - DFS can be implemented recursively or iteratively, but here I used recursion for simplicity.
Time: O(mn), Space: O(mn)
Notes: 
    - Early return if original color == target color to avoid infinite recursion.
    - Handle image boundaries and color match in the DFS base case.
Read Solution: No
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        def checkColor(imageList: List[List[int]], row: int, col: int):
            if row < 0 or row >= len(imageList) or col < 0 or col >= len(imageList[0]) \
            or imageList[row][col] != original:
                return
            
            imageList[row][col] = color
            checkColor(imageList, row-1, col)
            checkColor(imageList, row, col-1)
            checkColor(imageList, row+1, col)
            checkColor(imageList, row, col+1)

        checkColor(image, sr, sc)

        return image