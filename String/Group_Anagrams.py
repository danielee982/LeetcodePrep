"""
LeetCode #49: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Date: 07-14-2025
Approach:
    - Initially added everything to the list directly, which caused duplicates.
    - Learned to use a key (like sorted string) to group or filter properly.
    - Use a dictionary to group words by their sorted character tuple.
Time: O(n * k log k), Space: O(n * k)
Notes: 
    - Sorting each word ensures all anagrams map to the same key.  
    - Dictionary key can be a string (joined sorted characters) or a tuple.  
    - Using `defaultdict(list)` could simplify the logic.
Read Solution: No
"""

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            key = "".join(sorted(s))

            if not key in dic:
                temp = []
                temp.append(s)
                dic[key] = temp
            else:
                temp = dic[key]
                temp.append(s)
                dic[key] = temp
        
        return list(dic.values())