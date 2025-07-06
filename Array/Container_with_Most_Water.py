"""
LeetCode #11: container with most water
Link: https://leetcode.com/problems/container-with-most-water
Date: 07-06-2025
Approach:
    - Initially tried brute-force (checking all pairs), which results in O(n^2) time.
    - Improved it using the two-pointer approach:
        - Start with pointers at both ends of the array.
        - Move the pointer pointing to the shorter line inward, aiming to find a higher height.
Time: O(n), Space: O(1)
Notes:
    - Two-pointer method efficiently replaces brute-force in problems that involve range and comparisons from both ends.
    - The key insight: width always decreases, so we need to try to increase height by moving the shorter side.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[right], height[left]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area