"""
LeetCode #39: Combination Sum
Link: https://leetcode.com/problems/combination-sum
Date: 06-30-2025
My Initial Approach: 
    - Tried brute force but couldn’t determine how many nested loops were needed.  
    - Then tried recursion, but I kept iterating only the first element of `candidates`.  
    - My recursion was also inefficient and not well-structured.  
Solution Approach:
    - Use backtracking.  
    - If the current path sum equals `target`, add a copy of the path to the result and return.  
    - If the current sum exceeds the target, stop and backtrack.  
    - Use `path.pop()` to backtrack after exploring a path.  
Time: O(2^t), Space: O(t) => t = target // min (of candidates)
Notes: 
    - Always define the recursion base (exit) condition first.  
    - Defining a helper function inside the main function allows access to outer parameters like `res` without using global variables.  
Read Solution: Yes
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            elif total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)

        return res