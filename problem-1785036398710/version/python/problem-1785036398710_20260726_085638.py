# Last updated: 7/26/2026, 8:56:38 AM
1class Solution(object):
2    def largestInteger(self, n, s):
3        if s > 9 * n:
4            return -1
5        ans = ""
6
7        for i in range(n):
8            digit = min(9, s)
9            ans += str(digit)
10            s -= digit
11        return int(ans)
12        