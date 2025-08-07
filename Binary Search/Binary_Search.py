"""
LeetCode #704: Binary Search
Link: https://leetcode.com/problems/binary-search
Date: 08-07-2025
Approach: 
    - Use binary search to find the target in a sorted array.
    - By adjusting the left and right pointers based on the mid value, we can efficiently narrow down the search space.
Time: O(log n), Space: O(1)
Notes: 
    - Binary search is only applicable to sorted arrays.
    - Binary search can achieve logarithmic time complexity, making it very efficient for large datasets.
Difficulty: Easy
Read Solution: No
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1