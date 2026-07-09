# Last updated: 7/9/2026, 9:04:15 AM
class Solution:
    def isPalindrome(self, x):
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        # If number has even digits: x == reversed_half
        # If number has odd digits: x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10
