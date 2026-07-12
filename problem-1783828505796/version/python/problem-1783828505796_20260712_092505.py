# Last updated: 7/12/2026, 9:25:05 AM
1class Solution(object):
2    def secondsBetweenTimes(self, startTime, endTime):
3        def to_seconds(time):
4            h, m, s = map(int, time.split(":"))
5            return h * 3600 + m * 60 + s
6        start = to_seconds(startTime)
7        end = to_seconds(endTime)
8
9        if end >= start:
10            return end - start
11        else:
12            return(24 * 3600 - start) + end
13        