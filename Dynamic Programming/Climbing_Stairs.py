"""
LeetCode #70: Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs
Date: 08-25-2025
Approach:
    - My initial approach was using recursion with factorial, which was inefficient for large n.
    - Then, I used dynamic programming to build up the number of ways to reach each step.
Time: O(n), Space: O(1)
Notes: 
    - I learned that the problem can be reduced to finding the nth Fibonacci number.
Read Solution: Yes for optimization
"""

class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n

        prev, curr = 1, 1

        for i in range(2, n+1):
            temp = curr
            curr += prev
            prev = temp
            
        return curr