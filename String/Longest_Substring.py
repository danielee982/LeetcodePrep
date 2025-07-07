"""
LeetCode #3: Longest Substring Without Repeating Characters  
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters  
Date: 07-07-2025  
Approach:  
- My initial approach was brute-force: checking all substrings and updating the max length.  
- After reading the solution, I used a sliding window with a hashmap.  
- As we iterate, we store each character in a hashmap.  
- If a duplicate is found, move the left side of the window forward until the duplicate is removed.
Time Complexity: O(n)  
Space Complexity: O(1) (since the character set is limited to ASCII)
Notes:  
- In Python, a dictionary can act as a hashmap.  
- Sliding window is useful for keeping track of a valid substring without duplicates.  
- `dict.get(ch, 0)` helps avoid KeyError when checking unseen characters.
Read Solution: Yes to improve efficiency
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = left = 0
        count = {}

        for right, ch in enumerate(s):
            count[ch] = 1 + count.get(ch, 0)
            while count[ch] > 1:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length
        