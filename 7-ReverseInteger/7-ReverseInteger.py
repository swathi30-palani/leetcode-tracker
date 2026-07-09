# Last updated: 7/9/2026, 9:04:18 AM
class Solution:
    def reverse(self, x):
        INT_MIN = -2**31       # -2147483648
        INT_MAX = 2**31 - 1    # 2147483647

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before pushing the digit
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res
