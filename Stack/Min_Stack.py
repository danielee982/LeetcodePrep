"""
LeetCode 155: Min Stack
Link: https://leetcode.com/problems/min-stack/
Date: 08-02-2025
Approach: 
    - Initially, I used a single stack to store all elements and another stack to keep track of the minimum.
    - I realized that if the second stack has only the minimum element, it can be popped when the minimum is removed.
    - Therefore, I tried to keep track of minimum elements at each time to the second stack.
Time: O(1), Space: O(n)
Notes: 
    - Slicing can be used to check if the second stack is empty and to get the last element in constant time.
Read Solution: No
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack2:
            self.stack2.append(val)
        else:
            if val <= self.stack2[-1]:
                self.stack2.append(val)

    def pop(self) -> None:
        i = self.stack.pop()
        if self.stack2 and i == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1] if self.stack2 else self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()