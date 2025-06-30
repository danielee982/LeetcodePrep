"""
LeetCode #56: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/
Date: 06-30-2025
Approach: 
    - Initially, I used two nested while loops to create a merged interval if there is overlap in the middle of the list.
    - It worked but I could've opimized it by using one while loop and comparing and updating the result list directly.
Time: O(N), Space: O(N)
Notes:
    - After soring the list, I need to care about just the maxmimum value of an interval.
Read Solution: No
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res