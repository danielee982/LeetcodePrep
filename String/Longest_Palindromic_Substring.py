"""
LeetCode #5: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring
Date: 07-30-2025
Approach: Expand Around Center
    - At first, I tried using brute force to check all substrings, but it was too slow and I didn't handle odd and even-length centers correctly.
    - Instead, I used the expand around center technique.
    - For each index, expand around both single and double centers to find palindromes. Track the longest.
Time: O(n^2), Space: O(1)
Notes:
    - Check both odd and even-length centers.
    - Edge cases: single character, all same characters.
Read Solution: Yes
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s

        longest = s[0]
        
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest