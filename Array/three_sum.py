"""
LeetCode #15: 3Sum
Date: 2025-06-28
Link: https://leetcode.com/problems/3sum/

Approach:
- Brute-force approach caused time limit exceeded (O(n³)), so switched to two-pointer technique after sorting.
- Iterate through each number `nums[i]`, then apply two pointers (`left`, `right`) to find pairs such that the sum of three numbers is zero.
- To avoid duplicates:
  - Skip duplicate `nums[i]` elements during the main loop.
  - After finding a valid triplet, skip over duplicate values for both `left` and `right`.

Time Complexity: O(n²)
Space Complexity: O(1) (excluding the result list)

Notes:
- Efficient duplicate skipping is key in two-pointer problems.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if sum_3 == 0:
                    
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1

                elif sum_3 < 0:
                    left += 1
                    
                elif sum_3 > 0:
                    right -= 1

        return res