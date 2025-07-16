"""
LeetCode #36: Valid Sudoku  
Link: https://leetcode.com/problems/valid-sudoku/  
Date: 07-15-2025  
Approach:  
    - At first, I checked each row, column, and 3x3 box separately using three separate loops.  
    - After reading the solution, I simplified the code by checking all three at once during a single traversal using `defaultdict(set)`.  
    - Used `(r // 3, c // 3)` as the key to represent each 3x3 sub-box.
Time: O(1), since the board is always 9x9  
Space: O(1), constant space for 9 rows, 9 columns, and 9 boxes
Notes:  
    - `defaultdict(set)` is useful to avoid KeyError and initialize sets automatically.  
    - Learned how to map each cell to a 3x3 box using integer division: `(r // 3, c // 3)`  
    - Validity of the board can be checked in a single pass by updating and checking sets simultaneously.
Read Solution: Yes
"""


from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True