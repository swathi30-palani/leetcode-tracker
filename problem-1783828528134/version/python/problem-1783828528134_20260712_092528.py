# Last updated: 7/12/2026, 9:25:28 AM
1class Solution(object):
2    def maxConsistentColumns(self, grid, limit):
3        m = len(grid)
4        n = len(grid[0])
5        dp = [1] * n
6        for j in range(n):
7            for i in range(j):
8                ok = True
9                for r in range(m):
10                    if abs(grid[r][j] - grid[r][i]) > limit:
11                        ok = False
12                        break
13                if ok:
14                    dp[j] = max(dp[j] , dp[i] + 1)
15        return max(dp)