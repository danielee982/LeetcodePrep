"""
LeetCode #150: Evaluate Reverse Polish Notation
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation
Date: 08-01-2025
Approach: 
    - Use a stack to evaluate the expression.
    - At first, I tried to use two stacks to store operands and operators, but it was more complex than needed.
    - Instead, I used a single stack to handle both numbers and operations, processing operators as they appeared.
Time: O(n), Space: O(n)
Notes: 
    - Try to handle operators first since there are only four operations.
    - "The answer and all the intermediate calculations can be represented in a 32-bit integer." means we don't need to worry about overflow.
    - Edge cases: division by zero, negative numbers. => string.isdigit() does not handle negative numbers.
Read Solution: Yes
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif ch == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            elif ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(ch))
        
        return stack[0]
                