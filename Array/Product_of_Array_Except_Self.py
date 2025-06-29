"""
LeetCode #238: Product of Array Except Itself
Link: https://leetcode.com/problems/product-of-array-except-self
Date: 06-29-2025
Approach: 
    - Since division is not allowed and time complexity has to be O(n), I tried to use extra arrays.
    - I create an output array that will hold the product of all elements to the left of each index.
    - Then, I iterate through the array in reverse to multiply the output array with the product of elements to the right of each index.
Time: O(n), Space: O(1)
Notes: 
    - When time complexity is O(n), I can think of using extra arrays at first.
Read Solution: Yes
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        res = 1

        for i in range(len(nums)):
            output.append(res)
            res *= nums[i]

        res = 1
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= res
            res *= nums[i]

        return output