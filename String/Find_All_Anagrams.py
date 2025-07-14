"""
LeetCode #438: Find All Anagrams in a String
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string
Date: 07-14-2025
Approach:
    - Initially tried checking all substrings of length `len(p)`, but it was inefficient. 
    - Use a sliding window approach with two counters to track the frequency of characters in the current window and the target string.
Time: O(n), Space: O(1)
Notes: 
    - I can use `Counter` from the `collections` module to simplify frequency counting.
Read Solution: Yes
"""

from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        count_window = Counter(s[:len(p)])
        res = []
        
        i = 0
        j = len(p)

        while j <= len(s):
            if count_p == count_window:
                res.append(i)

            count_window[s[i]] -= 1
            if count_window[s[i]] <= 0:
                count_window.pop(s[i])
            
            if j < len(s):
                count_window[s[j]] += 1
            
            i += 1
            j += 1

        return res