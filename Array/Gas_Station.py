"""
LeetCode #134: Gas Station
Link: https://leetcode.com/problems/gas-station/
Date: 07-07-2025
Approach:  
    - My initial approach was simulating the circular path from each station, which caused time limit issues.  
    - After reading the solution, I used a greedy method with a single pass and two variables (`start`, `tank`) to track the valid starting point.  
    - If total gas is less than total cost, return -1 immediately.
Time: O(n), Space: O(1)
Notes:  
    - If a section fails (tank < 0), none of its stations can be a valid starting point.  
    - Passing through a failed station is fine ; you just can't start there.  
    - Learned how greedy + cumulative logic can replace circular simulation.
Read Solution: Yes
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        return start