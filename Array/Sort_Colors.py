"""
LeetCode #75: Sort Colors
Link: https://leetcode.com/problems/sort-colors
Date: 07-06-2025
Approach: 
    - My initial approach was selection sort (brute-force), which worked but had O(n^2) time complexity.
    - I read the official solution to improve time complexity and implemented the Dutch National Flag algorithm.
    - This uses three pointers: left, mid, and right to sort 0s, 1s, and 2s in one pass.
Time: O(n), Space: O(1)
Notes: 
    - `left`: points to the next position to place 0.
    - `mid`: current element being evaluated.
    - `right`: points to the next position to place 2.
    - When nums[mid] == 0, swap with left and move both left and mid.
    - When nums[mid] == 2, swap with right and move right only.
    - When nums[mid] == 1, just move mid.
Read Solution: Yes to imporve complexity
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        left = mid = 0
        right = len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            elif nums[mid] == 1:
                mid += 1