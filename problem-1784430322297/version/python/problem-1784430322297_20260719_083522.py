# Last updated: 7/19/2026, 8:35:22 AM
1class Solution(object):
2    def canReach(self, start, target):
3        sx, sy = start
4        tx, ty = target
5        return (sx + sy) % 2 == (tx + ty) % 2
6        