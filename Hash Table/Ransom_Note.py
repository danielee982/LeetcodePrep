"""
LeetCode #383: Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Date: 07-17-2025
Approach: 
    - Define a variable `count` to keep track of character frequencies in the `magazine`.
    - Iterate through each character in `ransomNote` and check if it exists in `count`.
Time: O(n), Space: O(1)
Notes: 
    - Counter from the collections module is also a kind of hash table.
Read Solution: No
"""

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count = Counter(magazine)

        for ch in ransomNote:
            if count[ch] == 0:
                return False
            else:
                count[ch] -= 1

        return True