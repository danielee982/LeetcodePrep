"""
LeetCode #57: Insert Interval
Link: https://leetcode.com/problems/insert-interval/
Date: 06-28-2025
My Initial Approach: 
    - merge new interval with all the existing intervals
    - Then, merge intervals if they overlap
    - In the end, the code got super messy and I had to take care of edge cases, which made it a lot harder than it actually is.
Solution Approach:
    - Iterate through the intervals and check if the new interval overlaps with the current interval.
    - If it doesn't, add the current interval to the result.
    - If it does, merge the intervals by updating the start and end of the new interval.
    - Finally, add the merged interval to the result.
    - After that, add the rest of the intervals to the result.
Time: O(n), Space: O(n)
Notes: 
    - Don't try to update and merge all intervals manually upfront
    - Realized that trying to "patch" existing intervals with multiple conditionals made it worse
Read Solution: Yes (after getting stuck for 3 hours)
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []

        # when there's no overlap, just add intervals
        while i < len(intervals) and intervals[i][1] <= newInterval[0]:
            res.append(intervals[i])
            i += 1

        # when intervals[i] has an overlap
        # iterate until they don't have overlaps
        # and merge the interval with newInterval if there is an overlap
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # add the merged interval
        res.append(newInterval)

        # add the rest of intervals
        res.extend(intervals[i:])
        return res