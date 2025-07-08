"""
LeetCode #8: String to Integer (atoi)  
Link: https://leetcode.com/problems/string-to-integer-atoi  
Date: 07-08-2025  
Approach:  
- I started by removing leading whitespace using `lstrip()`.  
- Then I manually handled the optional '+' or '-' sign.  
- After that, I collected digits one by one until a non-digit was found.  
- I built the number as a string and converted it at the end using `int()`.  
- Finally, I clamped the result to the 32-bit signed integer range.
Time Complexity: O(n), where n is the length of the string  
Space Complexity: O(n), due to the temporary result string
Notes:  
- No need to manually skip leading zeros since `int()` handles them.  
- Use `"".isdigit()` to safely check valid digits while building the number.  
- Sign handling can be done once before digit parsing.  
- Clamping ensures the result stays within [-2^31, 2^31 - 1].  
- The check `if res in ("", "-"):` avoids crashing on invalid input.
Read Solution: No
"""


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip() # step 1

        if len(s) == 0: return 0
        
        res = ""
        sign = 1
        i = 0

        # handle sign
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
                res += '-'
            i += 1

        # collect digits only
        while i < len(s) and s[i].isdigit():
            res += s[i]
            i += 1

        # check if res is a valid number
        if res in ("", "-"):
            return 0

        res = int(res)

        # clamp within 32-bit signed integer range
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1

        return res