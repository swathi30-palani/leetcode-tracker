# Last updated: 7/9/2026, 9:04:17 AM
class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check for optional sign
        sign = 1
        if i < n and s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Read digits and form the number
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return sign * num
