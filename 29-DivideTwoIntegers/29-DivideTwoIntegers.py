# Last updated: 7/9/2026, 9:03:38 AM
class Solution:
    def divide(self, dividend, divisor):
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Subtract divisor multiples from dividend
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= temp_divisor << 1:
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        return -quotient if negative else quotient
