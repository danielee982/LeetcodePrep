"""
LeetCode #20: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses
Date: 07-07-2025
Approach: 
    - Store the character from a given array if it's an open bracket.
    - If the character is a close bracket, check if it has a pair in stack.
Time: O(n), Space: O(n)
Notes: 
    - List does not have isEmpty method.
    - "if not [list]" can be used like isEmpty.
Read Solution: No
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif ch == ')':
                    if stack.pop() != '(':
                        return False
                elif ch == '}':
                    if stack.pop() != '{':
                        return False
                elif ch == ']':
                    if stack.pop() != '[':
                        return False

        if stack:
            return False
                
        return True