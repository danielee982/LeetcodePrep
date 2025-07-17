"""
LeetCode #232: Implement Queue Using Stacks
Link: https://leetcode.com/problems/implement-queue-using-stacks/
Date: 07-17-2025
Approach: [Briefly describe]
    - Use two stacks to implement a queue.
    - Stack1 is used for enqueue operations, and Stack2 is used for dequeue operations.
Time: O(1) amortized for push, O(n) for pop, Space: O(n)
Notes:
    - The worst-case time complexity for pop and peek operations is O(n) when all elements are transferred from stack1 to stack2.
Read Solution: Yes
"""

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()