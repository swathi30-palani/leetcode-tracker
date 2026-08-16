# Last updated: 8/16/2026, 9:22:57 AM
1class Solution:
2    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
3        max_light = max(lights)
4
5        max_waiting_time = 0
6
7        for arrival in arrivalTime:
8            r = arrival % period
9
10            if r >= max_light:
11                waiting_time = period - r
12                if waiting_time > max_waiting_time:
13                    max_waiting_time = waiting_time
14        return max_waiting_time