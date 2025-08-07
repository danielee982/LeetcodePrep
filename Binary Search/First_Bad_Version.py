"""
LeetCode #278: First Bad Version
Link: https://leetcode.com/problems/first-bad-version
Date: 08-07-2025
Approach: 
    - Use binary search to find the first bad version.
    - By adjusting the left and right pointers based on the mid value, we can efficiently narrow down the search space.
Time: O(log n), Space: O(1)
Notes: 
    - 
Read Solution: No
"""

# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            elif not isBadVersion(mid):
                left = mid + 1
                if isBadVersion(left):
                    return left

        return left